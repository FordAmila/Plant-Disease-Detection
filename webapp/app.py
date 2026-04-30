import streamlit as st
import cv2
import numpy as np
from PIL import Image
import tensorflow as tf
from tensorflow.keras.applications.efficientnet import preprocess_input
import os
import time
from datetime import datetime

# Import disease database
import sys
sys.path.append('utils')
from utils.disease_db import get_recommendations

# Page config
st.set_page_config(
    page_title="Plant Disease Detector | AI-Powered Diagnosis",
    page_icon="🌿",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ==================== CUSTOM CSS ====================
st.markdown("""
<style>
@import url('https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css');

/* Main Container */
.stApp {
    background: linear-gradient(135deg, #0a0f1c, #0f172a, #1e1b4b);
}

/* ==================== ENHANCED HEADER ==================== */
.main-header {
    text-align: center;
    padding: 2.5rem 2rem;
    background: linear-gradient(135deg, rgba(27,94,32,0.85), rgba(46,125,50,0.75));
    border-radius: 30px;
    margin-bottom: 2rem;
    position: relative;
    overflow: hidden;
    box-shadow: 0 20px 40px rgba(0,0,0,0.3);
}

.main-header::before {
    content: '';
    position: absolute;
    top: -50%;
    left: -50%;
    width: 200%;
    height: 200%;
    background: radial-gradient(circle, rgba(255,255,255,0.15) 0%, transparent 70%);
    animation: rotate 20s linear infinite;
}

@keyframes rotate {
    from { transform: rotate(0deg); }
    to { transform: rotate(360deg); }
}

.header-icon {
    font-size: 4rem;
    margin-bottom: 0.5rem;
    color: white;
    position: relative;
    z-index: 1;
    text-shadow: 0 0 20px rgba(255,255,255,0.5);
    animation: float 3s ease-in-out infinite;
}

@keyframes float {
    0%, 100% { transform: translateY(0px); }
    50% { transform: translateY(-10px); }
}

.main-header h1 {
    color: white;
    font-size: 2.8rem;
    margin: 0;
    font-weight: 800;
    position: relative;
    z-index: 1;
    letter-spacing: -0.5px;
    text-shadow: 2px 2px 4px rgba(0,0,0,0.2);
}

.main-header p {
    color: rgba(255,255,255,0.95);
    font-size: 1.1rem;
    margin-top: 0.5rem;
    position: relative;
    z-index: 1;
}

.stats-badge {
    display: flex;
    justify-content: center;
    gap: 1.2rem;
    margin-top: 1.5rem;
    flex-wrap: wrap;
    position: relative;
    z-index: 1;
}

.stat-badge {
    background: rgba(255,255,255,0.2);
    backdrop-filter: blur(10px);
    padding: 0.6rem 1.5rem;
    border-radius: 50px;
    font-size: 0.9rem;
    color: white;
    display: inline-flex;
    align-items: center;
    gap: 0.6rem;
    border: 1px solid rgba(255,255,255,0.3);
    font-weight: 600;
    transition: all 0.3s ease;
}

.stat-badge:hover {
    transform: translateY(-3px);
    background: rgba(255,255,255,0.3);
    border-color: rgba(255,255,255,0.5);
    box-shadow: 0 5px 15px rgba(0,0,0,0.2);
}

.stat-badge i {
    font-size: 1rem;
}

/* Glass Card */
.glass-card {
    background: rgba(15, 25, 35, 0.85);
    backdrop-filter: blur(12px);
    border-radius: 28px;
    padding: 24px;
    border: 1px solid rgba(255, 255, 255, 0.15);
    transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
    margin-bottom: 24px;
    box-shadow: 0 8px 32px rgba(0, 0, 0, 0.2);
}

.glass-card:hover {
    transform: translateY(-4px);
    border-color: rgba(5, 150, 105, 0.5);
    box-shadow: 0 20px 50px rgba(0, 0, 0, 0.3);
}

/* Section Title - CRYSTAL CLEAR */
.section-title {
    font-size: 1.4rem;
    font-weight: 800;
    color: #FFFFFF !important;
    margin-bottom: 1.5rem;
    padding-bottom: 0.75rem;
    border-bottom: 3px solid #10b981;
    display: flex;
    align-items: center;
    gap: 0.75rem;
    text-shadow: 0 0 5px rgba(0,0,0,0.3);
    letter-spacing: -0.3px;
}

.section-title i {
    color: #10b981;
    font-size: 1.5rem;
}

/* Left Container Header */
.left-container-header {
    display: flex;
    align-items: center;
    gap: 0.75rem;
    margin-bottom: 1.5rem;
}

.left-container-header i {
    font-size: 1.6rem;
    color: #10b981;
}

.left-container-header h3 {
    color: white !important;
    font-weight: 700 !important;
}

/* Buttons */
.stButton > button {
    background: linear-gradient(135deg, #059669, #10b981);
    color: white;
    border: none;
    padding: 12px 20px;
    font-weight: 700;
    border-radius: 12px;
    transition: all 0.3s ease;
    cursor: pointer;
    font-size: 14px;
    letter-spacing: 0.5px;
    width: 100%;
    box-shadow: 0 4px 15px rgba(5, 150, 105, 0.3);
}

.stButton > button:hover {
    transform: translateY(-3px);
    box-shadow: 0 8px 25px rgba(5, 150, 105, 0.5);
    background: linear-gradient(135deg, #10b981, #059669);
}

button[key="upload_btn"] {
    background: linear-gradient(135deg, #2563eb, #3b82f6);
    box-shadow: 0 4px 15px rgba(37, 99, 235, 0.3);
}

button[key="capture_btn"] {
    background: linear-gradient(135deg, #7c3aed, #8b5cf6);
    box-shadow: 0 4px 15px rgba(124, 58, 237, 0.3);
}

/* Divider */
.divider-light {
    height: 1px;
    background: linear-gradient(90deg, transparent, rgba(255,255,255,0.2), transparent);
    margin: 1rem 0;
}

/* Section Badge */
.section-badge {
    display: inline-flex;
    align-items: center;
    gap: 0.5rem;
    background: rgba(5, 150, 105, 0.25);
    padding: 0.5rem 1rem;
    border-radius: 20px;
    font-size: 0.8rem;
    margin-bottom: 1rem;
    color: #34d399;
    font-weight: 700;
    border: 1px solid rgba(5, 150, 105, 0.4);
}

/* Image Container */
.image-container-small {
    max-width: 100%;
    margin: 1rem 0;
    border-radius: 16px;
    overflow: hidden;
    background: rgba(0, 0, 0, 0.3);
    padding: 0.5rem;
    border: 1px solid rgba(255,255,255,0.1);
}

.image-container-small img {
    border-radius: 12px;
    max-height: 220px;
    object-fit: contain;
    width: 100%;
}

/* Upload Placeholder */
.upload-placeholder {
    text-align: center;
    padding: 2rem;
    background: rgba(255, 255, 255, 0.05);
    border-radius: 16px;
    border: 2px dashed rgba(5, 150, 105, 0.3);
    margin: 1rem 0;
}

.upload-placeholder i {
    font-size: 3rem;
    color: #10b981;
    margin-bottom: 1rem;
    opacity: 0.8;
}

.upload-placeholder p {
    margin: 0.5rem 0;
    color: rgba(255, 255, 255, 0.9);
    font-weight: 600;
}

.upload-placeholder small {
    color: rgba(255, 255, 255, 0.6);
    font-size: 0.75rem;
}

/* Selection Confirmation */
.selection-confirmation {
    display: flex;
    align-items: center;
    gap: 1rem;
    padding: 1rem;
    background: linear-gradient(135deg, rgba(5, 150, 105, 0.2), rgba(5, 150, 105, 0.08));
    border-radius: 12px;
    margin: 1rem 0;
    border-left: 3px solid #10b981;
}

.selection-confirmation i {
    font-size: 1.5rem;
    color: #10b981;
}

.confirmation-text {
    color: white;
    font-weight: 600;
}

.confirmation-text strong {
    font-size: 0.9rem;
    color: #FFFFFF;
}

/* Status Footer */
.status-footer {
    margin-top: 1.5rem;
    padding-top: 1rem;
    border-top: 1px solid rgba(255, 255, 255, 0.1);
    display: flex;
    justify-content: space-between;
    align-items: center;
}

.status-label {
    font-size: 0.85rem;
    color: rgba(255, 255, 255, 0.8);
    display: flex;
    align-items: center;
    gap: 0.5rem;
    font-weight: 600;
}

.status-value {
    font-size: 0.9rem;
    font-weight: 800;
    color: #34d399;
}

/* ==================== DIAGNOSIS RESULTS - CRYSTAL CLEAR ==================== */
.diagnosis-header {
    text-align: center;
    padding: 1.5rem;
    border-radius: 20px;
    margin-bottom: 1.5rem;
}

.status-healthy { background: linear-gradient(135deg, #065f46, #059669); }
.status-early { background: linear-gradient(135deg, #b45309, #ea580c); }
.status-moderate { background: linear-gradient(135deg, #c2410c, #f97316); }
.status-severe { background: linear-gradient(135deg, #be123c, #e11d48); }
.status-critical { background: linear-gradient(135deg, #881337, #be123c); }
.status-no-leaf { background: linear-gradient(135deg, #4b5563, #6b7280); }

.diagnosis-icon {
    font-size: 3.5rem;
    margin-bottom: 0.5rem;
}

.diagnosis-header h2 {
    color: #FFFFFF !important;
    font-size: 1.6rem;
    margin: 0.5rem 0;
    font-weight: 800;
    text-shadow: 1px 1px 2px rgba(0,0,0,0.2);
}

.diagnosis-meta {
    display: flex;
    justify-content: center;
    gap: 1rem;
    margin-top: 0.75rem;
    flex-wrap: wrap;
}

.meta-badge {
    background: rgba(255,255,255,0.25);
    padding: 0.4rem 1rem;
    border-radius: 25px;
    font-size: 0.8rem;
    color: white;
    display: inline-flex;
    align-items: center;
    gap: 0.4rem;
    font-weight: 700;
    letter-spacing: 0.3px;
}

/* Severity Section */
.severity-section {
    margin: 1.5rem 0;
}

.severity-label {
    font-size: 0.9rem;
    color: white;
    margin-bottom: 0.5rem;
    display: flex;
    align-items: center;
    gap: 0.5rem;
    font-weight: 600;
}

.severity-bar {
    height: 12px;
    background: rgba(255,255,255,0.2);
    border-radius: 6px;
    overflow: hidden;
    margin-bottom: 0.5rem;
}

.severity-fill {
    height: 100%;
    background: linear-gradient(90deg, #10b981, #f59e0b, #ef4444);
    border-radius: 6px;
    transition: width 0.8s cubic-bezier(0.4, 0, 0.2, 1);
}

.severity-value {
    font-size: 0.85rem;
    color: rgba(255,255,255,0.85);
    text-align: right;
    font-weight: 600;
}

/* Section Subtitle */
.section-subtitle {
    font-size: 1.1rem;
    font-weight: 800;
    color: #f0fdf4;
    margin: 1.2rem 0 0.8rem 0;
    display: flex;
    align-items: center;
    gap: 0.5rem;
}

/* Prediction Items */
.prediction-item {
    margin: 0.8rem 0;
    padding: 0.6rem;
    background: rgba(255,255,255,0.06);
    border-radius: 12px;
}

.prediction-header {
    display: flex;
    justify-content: space-between;
    margin-bottom: 0.5rem;
    font-size: 0.85rem;
}

.prediction-name {
    color: white;
    font-weight: 600;
}

.prediction-confidence {
    font-weight: 800;
}

.prediction-bar {
    height: 6px;
    background: rgba(255,255,255,0.15);
    border-radius: 3px;
    overflow: hidden;
}

.prediction-fill {
    height: 100%;
    border-radius: 3px;
    transition: width 0.5s ease;
}

/* Urgency Banner */
.urgency-banner {
    padding: 0.8rem 1rem;
    border-radius: 12px;
    text-align: center;
    margin: 1rem 0;
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 0.5rem;
}

.urgency-critical { background: rgba(190, 18, 60, 0.3); border: 1px solid rgba(190, 18, 60, 0.6); }
.urgency-high { background: rgba(234, 88, 12, 0.3); border: 1px solid rgba(234, 88, 12, 0.6); }
.urgency-medium { background: rgba(245, 158, 11, 0.3); border: 1px solid rgba(245, 158, 11, 0.6); }
.urgency-low { background: rgba(5, 150, 105, 0.3); border: 1px solid rgba(5, 150, 105, 0.6); }

.urgency-icon {
    font-size: 1.3rem;
}

.urgency-text {
    font-weight: 800;
    letter-spacing: 0.5px;
    font-size: 0.9rem;
    color: white;
}

/* Action Items */
.action-item, .treatment-item, .prevention-item {
    padding: 0.7rem 1rem;
    margin: 0.5rem 0;
    background: rgba(255,255,255,0.08);
    border-radius: 10px;
    border-left: 3px solid #10b981;
    transition: all 0.3s ease;
    font-size: 0.85rem;
    color: white;
    font-weight: 500;
}

.action-item:hover, .treatment-item:hover, .prevention-item:hover {
    transform: translateX(5px);
    background: rgba(255,255,255,0.12);
}

/* Option Content */
.option-content {
    font-size: 0.85rem;
    color: rgba(255,255,255,0.9);
    padding: 0.5rem;
    line-height: 1.5;
    font-weight: 500;
}

/* Pro Tip */
.pro-tip {
    background: linear-gradient(135deg, rgba(59, 130, 246, 0.25), rgba(59, 130, 246, 0.1));
    border-radius: 12px;
    padding: 1rem;
    margin: 1rem 0;
    display: flex;
    gap: 0.75rem;
    align-items: flex-start;
    border: 1px solid rgba(59, 130, 246, 0.5);
}

.tip-icon {
    font-size: 1.3rem;
    color: #60a5fa;
}

.tip-content {
    flex: 1;
    font-size: 0.85rem;
    line-height: 1.5;
    color: white;
    font-weight: 600;
}

/* Info Grid */
.info-grid {
    display: flex;
    gap: 0.75rem;
    margin: 1rem 0;
}

.info-item {
    flex: 1;
    text-align: center;
    padding: 0.75rem;
    background: rgba(255,255,255,0.08);
    border-radius: 12px;
    transition: all 0.3s ease;
}

.info-item:hover {
    background: rgba(255,255,255,0.12);
    transform: translateY(-2px);
}

.info-label {
    font-size: 0.7rem;
    color: rgba(255,255,255,0.8);
    text-transform: uppercase;
    margin-bottom: 0.25rem;
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 0.25rem;
    font-weight: 700;
}

.info-value {
    font-size: 0.95rem;
    font-weight: 800;
    color: #34d399;
}

/* Diagnosis Footer */
.diagnosis-footer {
    margin-top: 1.5rem;
    padding-top: 1rem;
    border-top: 1px solid rgba(255,255,255,0.1);
    display: flex;
    justify-content: space-between;
    align-items: center;
    flex-wrap: wrap;
    gap: 0.5rem;
    font-size: 0.75rem;
}

.timestamp {
    color: rgba(255,255,255,0.7);
    display: flex;
    align-items: center;
    gap: 0.25rem;
    font-weight: 600;
}

.disclaimer-text {
    color: rgba(255,255,255,0.6);
    display: flex;
    align-items: center;
    gap: 0.25rem;
    font-weight: 500;
}

/* Empty State */
.empty-state {
    text-align: center;
    padding: 3rem 1rem;
}

.empty-state i {
    font-size: 4.5rem;
    color: #34d399;
    margin-bottom: 1rem;
    opacity: 0.9;
}

.empty-state h3 {
    color: white;
    margin-bottom: 1rem;
    font-size: 1.3rem;
    font-weight: 800;
}

.empty-state p {
    color: rgba(255,255,255,0.8);
    margin-bottom: 1rem;
    font-weight: 500;
}

.steps-container {
    text-align: left;
    display: inline-block;
    margin-top: 1rem;
}

.step-item {
    display: flex;
    align-items: center;
    gap: 0.75rem;
    margin: 0.75rem 0;
    padding: 0.5rem 1rem;
    background: rgba(255, 255, 255, 0.08);
    border-radius: 10px;
    transition: all 0.3s ease;
}

.step-item:hover {
    background: rgba(255, 255, 255, 0.12);
    transform: translateX(5px);
}

.step-number {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    width: 28px;
    height: 28px;
    background: #10b981;
    color: white;
    border-radius: 50%;
    font-size: 0.8rem;
    font-weight: bold;
}

.step-item span:last-child {
    color: rgba(255,255,255,0.9);
    font-weight: 600;
}

/* History Section */
.history-section {
    margin: 2rem 0 1rem 0;
}

/* Stat Cards */
.stat-card {
    text-align: center;
    padding: 1rem;
    background: rgba(255,255,255,0.08);
    border-radius: 16px;
    transition: all 0.3s ease;
}

.stat-card:hover {
    transform: translateY(-3px);
    background: rgba(255,255,255,0.12);
}

.stat-value {
    font-size: 1.8rem;
    font-weight: 800;
    color: #34d399;
}

.stat-label {
    font-size: 0.7rem;
    color: rgba(255,255,255,0.8);
    margin-top: 0.25rem;
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 0.25rem;
    font-weight: 600;
}

/* History Card Enhanced */
.history-card-enhanced {
    background: rgba(255,255,255,0.08);
    border-radius: 12px;
    overflow: hidden;
    transition: all 0.3s ease;
    margin: 0.5rem 0;
}

.history-card-enhanced:hover {
    transform: translateY(-3px);
    background: rgba(255,255,255,0.12);
}

.history-card-header {
    padding: 0.75rem;
    border-bottom: 2px solid;
    display: flex;
    align-items: center;
    gap: 0.5rem;
}

.history-status-icon {
    font-size: 1rem;
}

.history-disease-name {
    font-weight: 700;
    font-size: 0.85rem;
    color: white;
    flex: 1;
}

.history-card-body {
    padding: 0.75rem;
}

.history-detail {
    font-size: 0.75rem;
    color: rgba(255,255,255,0.85);
    margin: 0.3rem 0;
    display: flex;
    align-items: center;
    gap: 0.5rem;
    font-weight: 500;
}

.history-detail i {
    width: 1rem;
    font-size: 0.7rem;
    color: #34d399;
}

.history-status-badge {
    display: inline-block;
    padding: 0.25rem 0.6rem;
    border-radius: 20px;
    font-size: 0.65rem;
    font-weight: 700;
    margin-top: 0.5rem;
}

/* ==================== ENHANCED FOOTER ==================== */
.footer {
    background: linear-gradient(135deg, rgba(6, 95, 70, 0.9), rgba(5, 150, 105, 0.8));
    backdrop-filter: blur(10px);
    border-radius: 20px;
    padding: 2rem;
    margin-top: 2rem;
    border: 1px solid rgba(255,255,255,0.2);
}

.footer-content {
    max-width: 1200px;
    margin: 0 auto;
    text-align: center;
}

.footer-logo {
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 0.75rem;
    margin-bottom: 1rem;
}

.footer-logo i {
    font-size: 2rem;
    color: white;
}

.footer-logo span {
    font-size: 1.2rem;
    font-weight: 700;
    color: white;
}

.footer-links {
    display: flex;
    justify-content: center;
    gap: 2rem;
    margin-bottom: 1rem;
    flex-wrap: wrap;
}

.footer-links a {
    color: rgba(255,255,255,0.8);
    text-decoration: none;
    font-size: 0.85rem;
    transition: all 0.3s ease;
    display: inline-flex;
    align-items: center;
    gap: 0.4rem;
}

.footer-links a:hover {
    color: white;
    transform: translateY(-2px);
}

.footer p {
    color: rgba(255,255,255,0.7);
    font-size: 0.8rem;
    margin: 0.5rem 0;
}

.footer .disclaimer {
    font-size: 0.7rem;
    opacity: 0.7;
    margin-top: 0.5rem;
}

.footer-divider {
    height: 1px;
    background: linear-gradient(90deg, transparent, rgba(255,255,255,0.3), transparent);
    margin: 1rem 0;
}

/* Toast Notification */
.toast-notification {
    position: fixed;
    bottom: 20px;
    right: 20px;
    background: linear-gradient(135deg, #059669, #10b981);
    color: white;
    padding: 0.75rem 1.5rem;
    border-radius: 50px;
    display: flex;
    align-items: center;
    gap: 0.5rem;
    z-index: 1000;
    box-shadow: 0 4px 20px rgba(0,0,0,0.3);
    animation: slideInRight 0.3s cubic-bezier(0.68, -0.55, 0.265, 1.55) forwards;
}

@keyframes slideInRight {
    from { transform: translateX(100%); opacity: 0; }
    to { transform: translateX(0); opacity: 1; }
}

/* Loading Container */
.loading-container {
    text-align: center;
    padding: 2rem;
    background: rgba(0,0,0,0.6);
    border-radius: 20px;
    backdrop-filter: blur(8px);
}

.loading-spinner {
    width: 50px;
    height: 50px;
    border: 3px solid rgba(255,255,255,0.2);
    border-top: 3px solid #10b981;
    border-right: 3px solid #f59e0b;
    border-radius: 50%;
    animation: spin 1s cubic-bezier(0.68, -0.55, 0.265, 1.55) infinite;
    margin: 0 auto 1rem;
}

@keyframes spin {
    from { transform: rotate(0deg); }
    to { transform: rotate(360deg); }
}

.loading-text {
    color: white;
    font-size: 0.9rem;
    font-weight: 600;
}

/* Streamlit Overrides */
.stSelectbox > div > div {
    background: rgba(15, 25, 35, 0.9);
    border-radius: 12px;
    border: 1px solid rgba(255, 255, 255, 0.15);
    color: white;
}

.stSelectbox label {
    color: rgba(255,255,255,0.9);
    font-weight: 600;
}

.stFileUploader > div {
    background: rgba(255, 255, 255, 0.05);
    border-radius: 16px;
    border: 2px dashed rgba(5, 150, 105, 0.4);
}

.stFileUploader > div:hover {
    background: rgba(255, 255, 255, 0.08);
    border-color: #10b981;
}

/* Expander Styling */
.streamlit-expanderHeader {
    background: rgba(255, 255, 255, 0.08);
    border-radius: 10px;
    font-weight: 700;
    color: white;
}

.streamlit-expanderHeader:hover {
    background: rgba(5, 150, 105, 0.2);
}

/* Scrollbar */
::-webkit-scrollbar {
    width: 8px;
    height: 8px;
}

::-webkit-scrollbar-track {
    background: rgba(255,255,255,0.05);
    border-radius: 10px;
}

::-webkit-scrollbar-thumb {
    background: rgba(5, 150, 105, 0.5);
    border-radius: 10px;
}

::-webkit-scrollbar-thumb:hover {
    background: rgba(5, 150, 105, 0.8);
}

/* Responsive */
@media (max-width: 768px) {
    .glass-card { padding: 16px; }
    .main-header h1 { font-size: 1.8rem; }
    .diagnosis-meta { flex-direction: column; align-items: center; gap: 0.5rem; }
    .diagnosis-footer { flex-direction: column; text-align: center; }
    .info-grid { flex-direction: column; }
    .section-title { font-size: 1.2rem; }
    .footer-links { gap: 1rem; }
}
</style>
""", unsafe_allow_html=True)

# ==================== DATA ====================
CLASS_NAMES = [
    'Apple___Apple_scab', 'Apple___Black_rot', 'Apple___Cedar_apple_rust', 'Apple___healthy',
    'Background_without_leaves', 'Blueberry___healthy', 'Cherry___Powdery_mildew', 'Cherry___healthy',
    'Corn___Cercospora_leaf_spot Gray_leaf_spot', 'Corn___Common_rust', 'Corn___Northern_Leaf_Blight', 'Corn___healthy',
    'Grape___Black_rot', 'Grape___Esca_(Black_Measles)', 'Grape___Leaf_blight_(Isariopsis_Leaf_Spot)', 'Grape___healthy',
    'Orange___Haunglongbing_(Citrus_greening)', 'Peach___Bacterial_spot', 'Peach___healthy',
    'Pepper,_bell___Bacterial_spot', 'Pepper,_bell___healthy', 'Potato___Early_blight', 'Potato___healthy', 'Potato___Late_blight',
    'Raspberry___healthy', 'Soybean___healthy', 'Squash___Powdery_mildew', 'Strawberry___healthy', 'Strawberry___Leaf_scorch',
    'Tomato___Bacterial_spot', 'Tomato___Early_blight', 'Tomato___healthy', 'Tomato___Late_blight', 'Tomato___Leaf_Mold',
    'Tomato___Septoria_leaf_spot', 'Tomato___Spider_mites Two-spotted_spider_mite', 'Tomato___Target_Spot',
    'Tomato___Tomato_mosaic_virus', 'Tomato___Tomato_Yellow_Leaf_Curl_Virus'
]

PLANT_OPTIONS = {
    " Apple": "Apple", " Blueberry": "Blueberry", " Cherry": "Cherry",
    " Corn": "Corn", " Grape": "Grape", " Orange": "Orange",
    " Peach": "Peach", " Pepper": "Pepper", " Potato": "Potato",
    " Raspberry": "Raspberry", " Soybean": "Soybean", " Squash": "Squash",
    " Strawberry": "Strawberry", " Tomato": "Tomato"
}

# ==================== SESSION STATE ====================
if 'result' not in st.session_state:
    st.session_state.result = None
if 'toast' not in st.session_state:
    st.session_state.toast = None
if 'scan_history' not in st.session_state:
    st.session_state.scan_history = []
if 'current_image' not in st.session_state:
    st.session_state.current_image = None
if 'top_predictions' not in st.session_state:
    st.session_state.top_predictions = None
if 'selected_plant' not in st.session_state:
    st.session_state.selected_plant = "Apple"  # Default to Apple
if 'uploader_key' not in st.session_state:
    st.session_state.uploader_key = 0
if 'active_section' not in st.session_state:
    st.session_state.active_section = "upload"
if 'image_loaded' not in st.session_state:
    st.session_state.image_loaded = False
if 'current_display_image' not in st.session_state:
    st.session_state.current_display_image = None

# ==================== HELPER FUNCTIONS ====================
def is_leaf_image(image):
    """Check if the image contains a leaf using color and edge detection"""
    try:
        if isinstance(image, Image.Image):
            image = np.array(image)
        
        # Convert to HSV for better color analysis
        hsv = cv2.cvtColor(image, cv2.COLOR_RGB2HSV)
        
        # Green color range detection (typical leaf color)
        lower_green = np.array([35, 40, 40])
        upper_green = np.array([85, 255, 255])
        green_mask = cv2.inRange(hsv, lower_green, upper_green)
        
        # Calculate percentage of green pixels
        green_percentage = np.sum(green_mask > 0) / (image.shape[0] * image.shape[1])
        
        # Edge detection for leaf shape
        gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
        edges = cv2.Canny(gray, 50, 150)
        edge_percentage = np.sum(edges > 0) / (image.shape[0] * image.shape[1])
        
        # A leaf typically has: 
        # - At least 15% green pixels
        # - Good amount of edges (leaf veins and boundaries)
        is_leaf = green_percentage > 0.15 and edge_percentage > 0.05
        
        return is_leaf, green_percentage, edge_percentage
    except Exception:
        return True, 0.5, 0.1  # Default to True if detection fails

def extract_plant_name(class_name):
    """Extract plant name from class name"""
    # Handle special cases first
    if class_name == 'Background_without_leaves':
        return 'Background'
    
    # Split by underscore and get the first part
    parts = class_name.split('___')
    if len(parts) > 1:
        plant_part = parts[0]
    else:
        plant_part = class_name.split('_')[0]
    
    # Map common variations to standard names
    plant_mapping = {
        'Apple': 'Apple',
        'Blueberry': 'Blueberry', 
        'Cherry': 'Cherry',
        'Corn': 'Corn',
        'Grape': 'Grape',
        'Orange': 'Orange',
        'Peach': 'Peach',
        'Pepper': 'Pepper',
        'Potato': 'Potato',
        'Raspberry': 'Raspberry',
        'Soybean': 'Soybean',
        'Squash': 'Squash',
        'Strawberry': 'Strawberry',
        'Tomato': 'Tomato'
    }
    
    # Try to match the plant name
    for key in plant_mapping:
        if key in plant_part:
            return plant_mapping[key]
    
    return plant_part

def extract_disease_name(class_name):
    """Extract disease name from class name"""
    if '___' in class_name:
        disease_part = class_name.split('___')[1]
        # Clean up disease name
        disease_part = disease_part.replace('_', ' ')
        # Handle specific disease names
        disease_mapping = {
            'Apple scab': 'Apple Scab',
            'Black rot': 'Black Rot',
            'Cedar apple rust': 'Cedar Apple Rust',
            'healthy': 'Healthy',
            'Powdery mildew': 'Powdery Mildew',
            'Cercospora leaf spot Gray leaf spot': 'Gray Leaf Spot',
            'Common rust': 'Common Rust',
            'Northern Leaf Blight': 'Northern Leaf Blight',
            'Esca Black Measles': 'Black Measles',
            'Leaf blight Isariopsis Leaf Spot': 'Leaf Blight',
            'Haunglongbing Citrus greening': 'Citrus Greening',
            'Bacterial spot': 'Bacterial Spot',
            'Early blight': 'Early Blight',
            'Late blight': 'Late Blight',
            'Leaf Mold': 'Leaf Mold',
            'Septoria leaf spot': 'Septoria Leaf Spot',
            'Spider mites Two spotted spider mite': 'Spider Mites',
            'Target Spot': 'Target Spot',
            'Tomato Yellow Leaf Curl Virus': 'Yellow Leaf Curl Virus',
            'Tomato mosaic virus': 'Mosaic Virus'
        }
        
        # Check for exact matches first
        for key, value in disease_mapping.items():
            if key.lower() in disease_part.lower():
                return value
        
        # Return formatted name
        words = disease_part.split()
        return ' '.join(word.capitalize() for word in words)
    
    return class_name.replace('_', ' ').title()

def is_healthy(class_name):
    """Check if the class indicates a healthy plant"""
    return 'healthy' in class_name.lower() or class_name == 'Background_without_leaves'

def apply_smart_weighting(predictions, class_names, selected_plant):
    """Apply weighting only when model is uncertain"""
    if not selected_plant or selected_plant == "Auto-detect":
        return predictions
    
    # Get top prediction
    top_idx = np.argmax(predictions)
    top_plant = extract_plant_name(class_names[top_idx])
    top_confidence = predictions[top_idx]
    
    # If model is very confident (>70%), trust it
    if top_confidence > 0.7:
        return predictions
    
    # If model is uncertain, apply gentle weighting
    weighted_preds = predictions.copy()
    for i, class_name in enumerate(class_names):
        plant = extract_plant_name(class_name)
        if plant == selected_plant:
            # Gentle boost for selected plant
            weighted_preds[i] *= 1.3
        elif plant != 'Unknown' and plant != top_plant and plant != 'Background':
            # Gentle reduction for other plants
            weighted_preds[i] *= 0.9
    
    # Renormalize
    return weighted_preds / weighted_preds.sum()

def get_top_predictions_with_plants(predictions, class_names, top_k=5):
    """Get top k predictions with plant and disease names"""
    top_indices = np.argsort(predictions)[-top_k:][::-1]
    results = []
    for idx in top_indices:
        class_name = class_names[idx]
        plant = extract_plant_name(class_name)
        disease = extract_disease_name(class_name)
        
        # Skip background in top predictions if there are better options
        if plant == 'Background' and len(results) > 0:
            continue
            
        results.append({
            'plant': plant,
            'disease': disease,
            'confidence': predictions[idx] * 100,
            'class_name': class_name
        })
    return results[:top_k]

@st.cache_resource
def load_model():
    try:
        if os.path.exists("Plant_Disease_Recog.keras"):
            return tf.keras.models.load_model("Plant_Disease_Recog.keras"), "keras", CLASS_NAMES
        elif os.path.exists("plant_disease_model.tflite"):
            interpreter = tf.lite.Interpreter(model_path="plant_disease_model.tflite")
            interpreter.allocate_tensors()
            return interpreter, "tflite", CLASS_NAMES
        return None, "demo", CLASS_NAMES
    except Exception:
        return None, "demo", CLASS_NAMES

def preprocess_image_keras(image, target_size=(224, 224)):
    if isinstance(image, Image.Image):
        image = np.array(image)
    if len(image.shape) == 2:
        image = cv2.cvtColor(image, cv2.COLOR_GRAY2RGB)
    elif image.shape[2] == 4:
        image = cv2.cvtColor(image, cv2.COLOR_RGBA2RGB)
    image = cv2.resize(image, target_size).astype(np.float32)
    return np.expand_dims(preprocess_input(image), axis=0)

def preprocess_image_tflite(image, target_size=(224, 224)):
    if isinstance(image, Image.Image):
        image = np.array(image)
    if len(image.shape) == 2:
        image = cv2.cvtColor(image, cv2.COLOR_GRAY2RGB)
    elif image.shape[2] == 4:
        image = cv2.cvtColor(image, cv2.COLOR_RGBA2RGB)
    return np.expand_dims(cv2.resize(image, target_size).astype(np.float32) / 255.0, axis=0)

def calculate_severity(image):
    try:
        if isinstance(image, Image.Image):
            image = np.array(image)
        hsv = cv2.cvtColor(image, cv2.COLOR_RGB2HSV)
        disease_mask = cv2.bitwise_or(
            cv2.inRange(hsv, np.array([10, 50, 50]), np.array([30, 255, 200])),
            cv2.inRange(hsv, np.array([20, 50, 50]), np.array([40, 255, 255]))
        )
        severity = (np.sum(disease_mask > 0) / (image.shape[0] * image.shape[1])) * 100
        return int(min(max(severity * 1.5, 5), 95))
    except Exception:
        return 45

def process_diagnosis(display_image):
    with st.spinner("Analyzing leaf image..."):
        loading_placeholder = st.empty()
        loading_placeholder.markdown("""
        <div class="loading-container">
            <div class="loading-spinner"></div>
            <div class="loading-text">Processing with EfficientNetB4...</div>
        </div>
        """, unsafe_allow_html=True)
        
        try:
            # Check if image contains a leaf
            is_leaf, green_pct, edge_pct = is_leaf_image(display_image)
            
            if not is_leaf:
                # Show non-leaf detection result
                loading_placeholder.empty()
                st.session_state.result = {
                    'plant': 'Unknown',
                    'disease': 'No Leaf Detected',
                    'confidence': 0.0,
                    'severity': 0,
                    'healthy': False,
                    'no_leaf': True,
                    'green_percentage': green_pct * 100,
                    'recommendations': {
                        'icon': '🍃',
                        'immediate': ['Please upload an image containing a plant leaf', 'Ensure the leaf is clearly visible', 'Try taking a photo with better lighting', 'Make sure the leaf is centered in the frame'],
                        'treatment': ['No treatment needed - this is not a plant leaf', 'Please capture a clear image of a plant leaf', 'Ensure good lighting and focus'],
                        'prevention': ['Use a plain background for better detection', 'Ensure the leaf is not too dark or too bright', 'Hold the camera steady when taking photos'],
                        'organic': 'N/A - No leaf detected',
                        'chemical': 'N/A - No leaf detected',
                        'urgency': 'LOW',
                        'timeframe': 'N/A',
                        'success_rate': 'N/A',
                        'tip': 'Make sure to capture a clear image of a plant leaf for accurate disease detection!'
                    },
                    'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                }
                st.session_state.toast = "no_leaf"
                loading_placeholder.empty()
                st.rerun()
                return
            
            # Proceed with normal diagnosis for leaf images
            model, model_type, class_names = load_model()
            
            if model_type == "keras":
                processed = preprocess_image_keras(display_image)
                raw_predictions = model.predict(processed, verbose=0)[0]
                predictions = apply_smart_weighting(raw_predictions, class_names, st.session_state.selected_plant)
            elif model_type == "tflite":
                processed = preprocess_image_tflite(display_image)
                model.set_tensor(model.get_input_details()[0]['index'], processed)
                model.invoke()
                raw_predictions = model.get_tensor(model.get_output_details()[0]['index'])[0]
                predictions = apply_smart_weighting(raw_predictions, class_names, st.session_state.selected_plant)
            else:
                np.random.seed(hash(str(display_image.tobytes())) % 2**32)
                predictions = np.random.dirichlet(np.ones(len(class_names)) * 0.5)
                if st.session_state.selected_plant != "Auto-detect":
                    for i, name in enumerate(class_names):
                        if extract_plant_name(name) == st.session_state.selected_plant:
                            predictions[i] += 0.5
                    predictions = predictions / predictions.sum()
            
            st.session_state.top_predictions = (predictions, class_names, st.session_state.selected_plant)
            top_idx = np.argmax(predictions)
            disease_class = class_names[top_idx]
            
            severity = calculate_severity(display_image)
            plant = extract_plant_name(disease_class)
            disease = extract_disease_name(disease_class)
            recommendations = get_recommendations(disease, severity, plant)
            
            st.session_state.result = {
                'plant': plant, 
                'disease': disease, 
                'confidence': float(predictions[top_idx]),
                'severity': severity, 
                'healthy': is_healthy(disease_class),
                'no_leaf': False,
                'recommendations': recommendations, 
                'selected_plant': st.session_state.selected_plant,
                'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            }
            
            st.session_state.scan_history.insert(0, {
                'disease': disease, 
                'plant': plant, 
                'severity': severity,
                'confidence': st.session_state.result['confidence'], 
                'healthy': st.session_state.result['healthy'],
                'no_leaf': False,
                'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            })
            st.session_state.scan_history = st.session_state.scan_history[:10]
            st.session_state.toast = "success"
            loading_placeholder.empty()
            st.rerun()
        except Exception as e:
            loading_placeholder.empty()
            st.error(f"Error during diagnosis: {str(e)}")

# ==================== HEADER ====================
st.markdown("""
<div class="main-header">
    <div class="header-icon"><i class="fas fa-seedling"></i></div>
    <h1>Plant Disease Detector</h1>
    <p>AI-Powered Plant Disease Detection & Treatment Recommendations</p>
    <div class="stats-badge">
        <span class="stat-badge"><i class="fas fa-bolt"></i> 92% Accuracy</span>
        <span class="stat-badge"><i class="fas fa-virus"></i> 38 Diseases</span>
        <span class="stat-badge"><i class="fas fa-microchip"></i> EfficientNetB4</span>
        <span class="stat-badge"><i class="fas fa-clock"></i> Real-time</span>
        <span class="stat-badge"><i class="fas fa-database"></i> 61K+ Images</span>
    </div>
</div>
""", unsafe_allow_html=True)

# ==================== MAIN LAYOUT ====================
col_left, col_right = st.columns([0.9, 1.1], gap="large")

# ==================== LEFT COLUMN ====================
with col_left:
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="left-container-header">
        <i class="fas fa-camera-retro"></i>
        <h3 class="section-title">Step 1: Upload or Capture Image</h3>
    </div>
    """, unsafe_allow_html=True)
    
    # Two action buttons (removed SELECT button)
    col1, col2 = st.columns(2)
    with col1:
        if st.button("📁 UPLOAD IMAGE", key="upload_btn", use_container_width=True):
            st.session_state.active_section = "upload"
            st.session_state.image_loaded = False
            st.rerun()
    with col2:
        if st.button("📷 CAPTURE PHOTO", key="capture_btn", use_container_width=True):
            st.session_state.active_section = "capture"
            st.session_state.image_loaded = False
            st.rerun()
    
    st.markdown('<div class="divider-light"></div>', unsafe_allow_html=True)
    
    # UPLOAD SECTION
    if st.session_state.active_section == "upload":
        st.markdown('<div class="section-badge"><i class="fas fa-cloud-upload-alt"></i> UPLOAD IMAGE</div>', unsafe_allow_html=True)
        
        uploaded_file = st.file_uploader(
            "Drag & drop or click to browse",
            type=["jpg", "jpeg", "png", "webp"],
            key=f"uploader_{st.session_state.uploader_key}",
            label_visibility="collapsed"
        )
        
        if uploaded_file:
            display_image = Image.open(uploaded_file)
            st.session_state.current_display_image = display_image
            st.session_state.image_loaded = True
            st.markdown('<div class="image-container-small">', unsafe_allow_html=True)
            st.image(display_image, use_container_width=True)
            st.markdown('</div>', unsafe_allow_html=True)
        else:
            st.session_state.image_loaded = False
            st.markdown("""
            <div class="upload-placeholder">
                <i class="fas fa-cloud-upload-alt"></i>
                <p><strong>No image selected</strong></p>
                <small>Upload a leaf image to begin diagnosis</small>
            </div>
            """, unsafe_allow_html=True)
    
    # CAPTURE SECTION
    elif st.session_state.active_section == "capture":
        st.markdown('<div class="section-badge"><i class="fas fa-camera"></i> CAPTURE PHOTO</div>', unsafe_allow_html=True)
        
        camera_image = st.camera_input("Position leaf in frame", label_visibility="collapsed")
        
        if camera_image:
            display_image = Image.open(camera_image)
            st.session_state.current_display_image = display_image
            st.session_state.image_loaded = True
            st.markdown('<div class="image-container-small">', unsafe_allow_html=True)
            st.image(display_image, use_container_width=True)
            st.markdown('</div>', unsafe_allow_html=True)
        else:
            st.session_state.image_loaded = False
            st.markdown("""
            <div class="upload-placeholder">
                <i class="fas fa-camera"></i>
                <p><strong>Ready to capture</strong></p>
                <small>Click the camera button above to take a photo of a plant leaf</small>
            </div>
            """, unsafe_allow_html=True)
    
    # Step 2: Select Plant Type (only shows after image is loaded)
    if st.session_state.image_loaded and st.session_state.current_display_image:
        st.markdown('<div class="divider-light"></div>', unsafe_allow_html=True)
        st.markdown("""
        <div class="left-container-header">
            <i class="fas fa-seedling"></i>
            <h3 class="section-title">Step 2: Select Plant Type</h3>
        </div>
        """, unsafe_allow_html=True)
        
        plant_display_options = list(PLANT_OPTIONS.keys())
        
        selected_display = st.selectbox(
            "Choose your plant type",
            options=plant_display_options,
            index=list(PLANT_OPTIONS.values()).index(st.session_state.selected_plant) if st.session_state.selected_plant in PLANT_OPTIONS.values() else 0,
            label_visibility="collapsed"
        )
        
        st.session_state.selected_plant = PLANT_OPTIONS[selected_display]
        
        st.markdown(f"""
        <div class="selection-confirmation">
            <i class="fas fa-check-circle"></i>
            <div class="confirmation-text">
                <strong>✓ Selected Plant</strong><br>
                {selected_display}
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        # Diagnose Button
        if st.button(" DIAGNOSE DISEASE", type="primary", use_container_width=True):
            process_diagnosis(st.session_state.current_display_image)
    
    st.markdown('</div>', unsafe_allow_html=True)

# ==================== RIGHT COLUMN - DIAGNOSIS RESULTS ====================
with col_right:
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    st.markdown('<h3 class="section-title"><i class="fas fa-chart-line"></i> Diagnosis Results</h3>', unsafe_allow_html=True)
    
    if st.session_state.result:
        r = st.session_state.result
        
        # Handle No Leaf Detection
        if r.get('no_leaf', False):
            st.markdown(f"""
            <div class="diagnosis-header status-no-leaf">
                <div class="diagnosis-icon">🍃❌</div>
                <h2>⚠️ No Leaf Detected</h2>
                <div class="diagnosis-meta">
                    <span class="meta-badge"><i class="fas fa-percent"></i> Green: {r.get('green_percentage', 0):.1f}%</span>
                    <span class="meta-badge"><i class="fas fa-image"></i> Invalid Image</span>
                </div>
            </div>
            """, unsafe_allow_html=True)
            
            st.markdown("""
            <div class="severity-section">
                <div class="severity-label"><i class="fas fa-info-circle"></i> Detection Result</div>
                <div class="severity-bar"><div class="severity-fill" style="width: 100%; background: linear-gradient(90deg, #6b7280, #9ca3af);"></div></div>
                <div class="severity-value">No plant leaf detected in this image</div>
            </div>
            """, unsafe_allow_html=True)
            
            rec = r['recommendations']
            
            st.markdown('<div class="section-subtitle"><i class="fas fa-lightbulb"></i> Suggestions</div>', unsafe_allow_html=True)
            
            with st.expander("📸 How to Take a Good Leaf Photo", expanded=True):
                for action in rec.get('immediate', [])[:4]:
                    st.markdown(f'<div class="action-item">• {action}</div>', unsafe_allow_html=True)
            
            with st.expander("💡 Pro Tips", expanded=False):
                for tip in rec.get('prevention', [])[:3]:
                    st.markdown(f'<div class="treatment-item">• {tip}</div>', unsafe_allow_html=True)
            
            st.markdown(f"""
            <div class="pro-tip">
                <div class="tip-icon"><i class="fas fa-lightbulb"></i></div>
                <div class="tip-content"><strong>Pro Tip:</strong> {rec.get('tip', 'Make sure to capture a clear image of a plant leaf for accurate disease detection!')}</div>
            </div>
            """, unsafe_allow_html=True)
            
            if st.button("🔄 Try Again", use_container_width=True):
                st.session_state.result = None
                st.session_state.image_loaded = False
                st.session_state.current_display_image = None
                st.rerun()
        else:
            rec = r['recommendations']
            
            # Status for leaf images
            if r['healthy']:
                status_class, status_text, status_icon = "status-healthy", "HEALTHY", "✅"
            elif r['severity'] < 20:
                status_class, status_text, status_icon = "status-early", "EARLY STAGE", "🟡"
            elif r['severity'] < 50:
                status_class, status_text, status_icon = "status-moderate", "MODERATE", "🟠"
            elif r['severity'] < 75:
                status_class, status_text, status_icon = "status-severe", "SEVERE", "🔴"
            else:
                status_class, status_text, status_icon = "status-critical", "CRITICAL", "💀"
            
            st.markdown(f"""
            <div class="diagnosis-header {status_class}">
                <div class="diagnosis-icon">{rec.get('icon', '🌿')}</div>
                <h2>{status_icon} {r['disease']}</h2>
                <div class="diagnosis-meta">
                    <span class="meta-badge"><i class="fas fa-leaf"></i> {r['plant']}</span>
                    <span class="meta-badge"><i class="fas fa-chart-simple"></i> {status_text}</span>
                    <span class="meta-badge"><i class="fas fa-bullseye"></i> {r['confidence']*100:.1f}%</span>
                </div>
            </div>
            """, unsafe_allow_html=True)
            
            # Severity Bar
            st.markdown(f"""
            <div class="severity-section">
                <div class="severity-label"><i class="fas fa-tachometer-alt"></i> Disease Severity</div>
                <div class="severity-bar"><div class="severity-fill" style="width: {r['severity']}%;"></div></div>
                <div class="severity-value">{r['severity']}% Affected Area</div>
            </div>
            """, unsafe_allow_html=True)
            
            # Top Predictions
            if st.session_state.top_predictions:
                st.markdown('<div class="section-subtitle"><i class="fas fa-chart-line"></i> Top Predictions</div>', unsafe_allow_html=True)
                preds, names, selected = st.session_state.top_predictions
                for i, result in enumerate(get_top_predictions_with_plants(preds, names, 3)):
                    color = "#10b981" if selected != "Auto-detect" and result['plant'] == selected else "#f59e0b" if result['confidence'] > 40 else "#ef4444"
                    st.markdown(f"""
                    <div class="prediction-item">
                        <div class="prediction-header">
                            <span class="prediction-name">#{i+1} {result['plant']} - {result['disease'][:35]}</span>
                            <span class="prediction-confidence" style="color: {color};">{result['confidence']:.1f}%</span>
                        </div>
                        <div class="prediction-bar"><div class="prediction-fill" style="width: {result['confidence']}%; background: {color};"></div></div>
                    </div>
                    """, unsafe_allow_html=True)
            
            # Treatment Recommendations
            st.markdown('<div class="section-subtitle"><i class="fas fa-clinic-medical"></i> Treatment Plan</div>', unsafe_allow_html=True)
            
            urgency_config = {
                "CRITICAL": ("urgency-critical", "", "CRITICAL - Take Action Immediately"),
                "HIGH": ("urgency-high", "", "HIGH - Treat Within 24-48 Hours"),
                "MEDIUM": ("urgency-medium", "", "MEDIUM - Treat Within 5-7 Days"),
                "LOW": ("urgency-low", "", "LOW - Monitor and Prevent")
            }
            urgency_class, urgency_icon, urgency_text = urgency_config.get(rec.get('urgency', 'MEDIUM'), urgency_config["MEDIUM"])
            st.markdown(f'<div class="urgency-banner {urgency_class}"><span class="urgency-icon">{urgency_icon}</span><span class="urgency-text">{urgency_text}</span></div>', unsafe_allow_html=True)
            
            # Two columns for treatment
            col_t1, col_t2 = st.columns(2)
            with col_t1:
                with st.expander(" Immediate Actions", expanded=True):
                    for action in rec.get('immediate', [])[:3]:
                        st.markdown(f'<div class="action-item">• {action}</div>', unsafe_allow_html=True)
                with st.expander(" Organic Solutions", expanded=False):
                    st.markdown(f'<div class="option-content">{rec.get("organic", "Neem oil spray")}</div>', unsafe_allow_html=True)
            
            with col_t2:
                with st.expander(" Treatment Plan", expanded=True):
                    for treatment in rec.get('treatment', [])[:3]:
                        st.markdown(f'<div class="treatment-item">• {treatment}</div>', unsafe_allow_html=True)
                with st.expander(" Conventional Solutions", expanded=False):
                    st.markdown(f'<div class="option-content">{rec.get("chemical", "Copper fungicide")}</div>', unsafe_allow_html=True)
            
            # Prevention
            with st.expander(" Prevention Tips", expanded=False):
                for prevention in rec.get('prevention', [])[:4]:
                    st.markdown(f'<div class="prevention-item">• {prevention}</div>', unsafe_allow_html=True)
            
            # Pro Tip & Info
            st.markdown(f"""
            <div class="pro-tip">
                <div class="tip-icon"><i class="fas fa-lightbulb"></i></div>
                <div class="tip-content"><strong>Pro Tip:</strong> {rec.get('tip', 'Early detection and treatment yields best results!')}</div>
            </div>
            """, unsafe_allow_html=True)
            
            st.markdown(f"""
            <div class="info-grid">
                <div class="info-item">
                    <span class="info-label"><i class="fas fa-hourglass-half"></i> Treatment Time</span>
                    <span class="info-value">{rec.get('timeframe', '7-10 days')}</span>
                </div>
                <div class="info-item">
                    <span class="info-label"><i class="fas fa-chart-line"></i> Success Rate</span>
                    <span class="info-value">{rec.get('success_rate', '85-90%')}</span>
                </div>
            </div>
            """, unsafe_allow_html=True)
            
            st.markdown(f'<div class="diagnosis-footer"><span class="timestamp"><i class="fas fa-calendar-alt"></i> Diagnosed: {r["timestamp"]}</span><span class="disclaimer-text"><i class="fas fa-exclamation-triangle"></i> AI-assisted - Consult expert</span></div>', unsafe_allow_html=True)
            
            if st.button(" New Diagnosis", use_container_width=True):
                st.session_state.result = None
                st.session_state.current_image = None
                st.session_state.top_predictions = None
                st.session_state.image_loaded = False
                st.session_state.current_display_image = None
                st.rerun()
    else:
        st.markdown("""
        <div class="empty-state">
            <i class="fas fa-microscope"></i>
            <h3>Ready for Diagnosis</h3>
            <p>Follow these steps:</p>
            <div class="steps-container">
                <div class="step-item"><span class="step-number">1</span><span>Upload or capture a leaf image</span></div>
                <div class="step-item"><span class="step-number">2</span><span>Select your plant type</span></div>
                <div class="step-item"><span class="step-number">3</span><span>Click Diagnose for analysis</span></div>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown('</div>', unsafe_allow_html=True)

# ==================== RECENT SCANS ====================
if st.session_state.scan_history:
    # Filter out non-leaf scans from history display
    valid_scans = [s for s in st.session_state.scan_history if not s.get('no_leaf', False)]
    
    if valid_scans:
        st.markdown('<div class="history-section"><h3 class="section-title"><i class="fas fa-history"></i> Recent Diagnoses</h3></div>', unsafe_allow_html=True)
        
        total_scans = len(valid_scans)
        healthy_scans = sum(1 for s in valid_scans if s.get('healthy', False))
        avg_confidence = sum(s['confidence'] for s in valid_scans) / total_scans if total_scans > 0 else 0
        
        col_s1, col_s2, col_s3, col_s4 = st.columns(4)
        with col_s1:
            st.markdown(f'<div class="stat-card"><div class="stat-value">{total_scans}</div><div class="stat-label"><i class="fas fa-chart-simple"></i> Total</div></div>', unsafe_allow_html=True)
        with col_s2:
            st.markdown(f'<div class="stat-card"><div class="stat-value">{healthy_scans}</div><div class="stat-label"><i class="fas fa-check-circle"></i> Healthy</div></div>', unsafe_allow_html=True)
        with col_s3:
            st.markdown(f'<div class="stat-card"><div class="stat-value">{total_scans - healthy_scans}</div><div class="stat-label"><i class="fas fa-exclamation-triangle"></i> Diseased</div></div>', unsafe_allow_html=True)
        with col_s4:
            st.markdown(f'<div class="stat-card"><div class="stat-value">{avg_confidence*100:.0f}%</div><div class="stat-label"><i class="fas fa-bullseye"></i> Avg Conf</div></div>', unsafe_allow_html=True)
        
        cols = st.columns(min(3, len(valid_scans)))
        for idx, scan in enumerate(valid_scans[:3]):
            with cols[idx]:
                severity_color = "#10b981" if scan['severity'] < 30 else "#f59e0b" if scan['severity'] < 60 else "#ef4444"
                st.markdown(f"""
                <div class="history-card-enhanced">
                    <div class="history-card-header" style="border-bottom-color: {severity_color};">
                        <span class="history-status-icon">{'✅' if scan.get('healthy', False) else '⚠️'}</span>
                        <span class="history-disease-name">{scan['disease'][:30]}</span>
                    </div>
                    <div class="history-card-body">
                        <div class="history-detail"><i class="fas fa-leaf"></i> {scan['plant']}</div>
                        <div class="history-detail"><i class="fas fa-bullseye"></i> {scan['confidence']*100:.1f}%</div>
                        <div class="history-detail"><i class="fas fa-tachometer-alt"></i> {scan['severity']}%</div>
                        <div class="history-detail"><i class="fas fa-calendar"></i> {scan['timestamp'][5:16]}</div>
                        <div class="history-status-badge" style="background: {severity_color}20; color: {severity_color};">{'Healthy' if scan.get('healthy', False) else 'Diseased'}</div>
                    </div>
                </div>
                """, unsafe_allow_html=True)

# ==================== ENHANCED FOOTER ====================
st.markdown("""
<div class="footer">
    <div class="footer-content">
        <div class="footer-logo">
            <i class="fas fa-leaf"></i>
            <span>Plant Disease Detector</span>
        </div>
        <div class="footer-divider"></div>
        <div class="footer-links">
            <a href="https://github.com/"><i class="fab fa-github"></i> GitHub</a>
            <a href="https://www.facebook.com/"><i class="fab fa-facebook"></i> Facebook</a>
            <a href="mailto:acliffordclint@gmail.com"><i class="fas fa-envelope"></i> Contact</a>
        </div>
        <p><i class="fas fa-microchip"></i> Powered by EfficientNetB4 | <i class="fas fa-database"></i> 39 Classes, 61,486 Images</p>
        <p class="disclaimer"><i class="fas fa-exclamation-triangle"></i> AI-assisted diagnostic tool - For professional advice, consult a plant pathologist</p>
        <p class="disclaimer" style="margin-top: 0.5rem;">© 2026 Plant Disease Detector | All Rights Reserved</p>
    </div>
</div>
""", unsafe_allow_html=True)

# Toast notification
if st.session_state.toast == "success":
    toast = st.empty()
    toast.markdown("""
    <div class="toast-notification">
        <i class="fas fa-check-circle"></i>
        <span>Diagnosis Complete!</span>
    </div>
    """, unsafe_allow_html=True)
    time.sleep(3)
    toast.empty()
    st.session_state.toast = None
elif st.session_state.toast == "no_leaf":
    toast = st.empty()
    toast.markdown("""
    <div class="toast-notification">
        <i class="fas fa-exclamation-triangle"></i>
        <span>No leaf detected! Please upload a plant leaf image.</span>
    </div>
    """, unsafe_allow_html=True)
    time.sleep(3)
    toast.empty()
    st.session_state.toast = None