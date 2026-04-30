// Redirect URL - Update this to your actual web app URL
const WEB_APP_URL = 'http://localhost:8501';

function redirectToWebApp() {
    window.location.href = WEB_APP_URL;
}

// Modal functionality
const modal = document.getElementById('redirectModal');
const openAppBtn = document.getElementById('openAppBtn');
const heroOpenAppBtn = document.getElementById('heroOpenAppBtn');
const quickScanBtn = document.getElementById('quickScanBtn');
const closeModal = document.getElementById('closeModal');
const cancelModal = document.getElementById('cancelModal');
const confirmRedirect = document.getElementById('confirmRedirect');

if (openAppBtn) openAppBtn.addEventListener('click', () => modal.classList.add('show'));
if (heroOpenAppBtn) heroOpenAppBtn.addEventListener('click', () => modal.classList.add('show'));
if (quickScanBtn) quickScanBtn.addEventListener('click', () => modal.classList.add('show'));
if (closeModal) closeModal.addEventListener('click', () => modal.classList.remove('show'));
if (cancelModal) cancelModal.addEventListener('click', () => modal.classList.remove('show'));
if (confirmRedirect) confirmRedirect.addEventListener('click', redirectToWebApp);

// Close modal when clicking outside
window.addEventListener('click', (e) => {
    if (e.target === modal) modal.classList.remove('show');
});

// Animate elements on scroll
const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.style.opacity = '1';
            entry.target.style.transform = 'translateY(0)';
            observer.unobserve(entry.target);
        }
    });
}, { threshold: 0.1, rootMargin: '0px 0px -50px 0px' });

document.querySelectorAll('.stat-card, .scan-card, .feature-card, .action-card, .featured-card').forEach(el => {
    el.style.opacity = '0';
    el.style.transform = 'translateY(20px)';
    el.style.transition = 'all 0.6s ease';
    observer.observe(el);
});

// Keyboard shortcut: Ctrl+K
document.addEventListener('keydown', (e) => {
    if (e.ctrlKey && e.key === 'k') {
        e.preventDefault();
        modal.classList.add('show');
    }
});

console.log('🌿 Plant Disease Detector Dashboard Ready!');