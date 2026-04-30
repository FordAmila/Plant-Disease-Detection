# Disease database with comprehensive recommendations for all 39 plant diseases

DISEASE_RECOMMENDATIONS = {
    # ==================== APPLE DISEASES ====================
    "Apple scab": {
        "name": "Apple Scab",
        "icon": "🍎",
        "immediate": [
            "Remove and destroy infected leaves immediately",
            "Rake up and dispose of fallen leaves",
            "Do not compost infected plant material"
        ],
        "treatment": [
            "Apply fungicide containing myclobutanil or captan",
            "Spray every 7-10 days during wet weather",
            "Apply lime sulfur during dormant season"
        ],
        "prevention": [
            "Plant resistant varieties like 'Liberty' or 'Enterprise'",
            "Prune trees for good air circulation",
            "Clean up fallen leaves in autumn",
            "Apply preventative fungicides in spring at green tip stage"
        ],
        "organic": "Sulfur spray, neem oil, or copper fungicide",
        "chemical": "Myclobutanil, Captan, or Fenbuconazole",
        "tip": "Apple scab overwinters in fallen leaves. Clean up is critical!",
        "timeframe": "Treat within 5-7 days",
        "success_rate": "85-90% with early treatment"
    },
    "Black rot": {
        "name": "Black Rot",
        "icon": "🍎",
        "immediate": [
            "Prune out infected branches 4-6 inches below visible symptoms",
            "Remove all infected fruit from tree and ground",
            "Disinfect pruning tools between cuts"
        ],
        "treatment": [
            "Apply captan or myclobutanil fungicide",
            "Begin treatment at bud break",
            "Continue every 10-14 days until harvest"
        ],
        "prevention": [
            "Remove mummified fruit from trees",
            "Prune to improve air circulation",
            "Avoid overhead irrigation",
            "Apply dormant oil in late winter"
        ],
        "organic": "Copper fungicide or sulfur",
        "chemical": "Captan, Myclobutanil, or Thiophanate-methyl",
        "tip": "Black rot fungi can survive in mummified fruit for up to 2 years!",
        "timeframe": "Treat immediately",
        "success_rate": "75-80% with aggressive treatment"
    },
    "Cedar apple rust": {
        "name": "Cedar Apple Rust",
        "icon": "🍎",
        "immediate": [
            "Remove infected leaves showing orange spots",
            "Check nearby juniper/cedar trees for galls",
            "Prune galls from cedars in winter"
        ],
        "treatment": [
            "Apply myclobutanil or propiconazole",
            "Spray every 7-10 days during wet spring weather",
            "Protect leaves before symptoms appear"
        ],
        "prevention": [
            "Remove cedar trees within 1 mile if possible",
            "Plant resistant apple varieties",
            "Apply fungicides from pink bud through petal fall",
            "Prune cedars to remove galls"
        ],
        "organic": "Sulfur or neem oil",
        "chemical": "Myclobutanil or Propiconazole",
        "tip": "This fungus needs both apple and cedar trees to complete its life cycle!",
        "timeframe": "Treat before symptoms appear",
        "success_rate": "90% with preventative treatment"
    },
    "Apple healthy": {
        "name": "Healthy Apple Tree",
        "icon": "🍎✅",
        "immediate": ["Continue your good care routine", "Monitor weekly for any changes"],
        "treatment": ["Maintain proper watering and fertilization", "Regular inspection and pruning"],
        "prevention": ["Annual dormant oil spray", "Clean up fallen fruit and leaves", "Prune annually for good air circulation"],
        "organic": "Compost tea application monthly",
        "chemical": "No treatment needed",
        "tip": "Healthy trees resist diseases better. Keep up the good work!",
        "timeframe": "No immediate action needed",
        "success_rate": "100% - Plant is healthy"
    },

    # ==================== BLUEBERRY DISEASES ====================
    "Blueberry healthy": {
        "name": "Healthy Blueberry",
        "icon": "🫐✅",
        "immediate": ["Continue proper care", "Monitor for pests"],
        "treatment": ["Maintain acidic soil (pH 4.5-5.5)", "Regular watering and mulching"],
        "prevention": ["Test soil pH annually", "Apply sulfur if needed", "Mulch with pine needles"],
        "organic": "Compost and organic fertilizer",
        "chemical": "No treatment needed",
        "tip": "Blueberries need acidic soil. Test pH regularly!",
        "timeframe": "No immediate action needed",
        "success_rate": "100% - Plant is healthy"
    },

    # ==================== CHERRY DISEASES ====================
    "Powdery mildew": {
        "name": "Powdery Mildew",
        "icon": "🍒",
        "immediate": [
            "Remove severely infected leaves",
            "Increase air circulation immediately",
            "Isolate infected plants"
        ],
        "treatment": [
            "Apply sulfur-based fungicide",
            "Use baking soda spray (1 tbsp per gallon water + few drops soap)",
            "Apply potassium bicarbonate",
            "Repeat weekly until controlled"
        ],
        "prevention": [
            "Water early morning so leaves dry quickly",
            "Ensure good sun exposure",
            "Avoid high-nitrogen fertilizers",
            "Space plants for air flow",
            "Use resistant varieties"
        ],
        "organic": "Milk spray (40% milk, 60% water) or neem oil",
        "chemical": "Sulfur, Potassium bicarbonate, or Myclobutanil",
        "tip": "Powdery mildew doesn't need free water to infect. It loves high humidity!",
        "timeframe": "Treat within 7 days",
        "success_rate": "90% with early treatment"
    },
    "Cherry healthy": {
        "name": "Healthy Cherry Tree",
        "icon": "🍒✅",
        "immediate": ["Continue good care routine", "Monitor for pests"],
        "treatment": ["Regular watering during fruit development", "Annual pruning"],
        "prevention": ["Apply dormant oil in late winter", "Clean up fallen fruit"],
        "organic": "Compost mulch around base",
        "chemical": "No treatment needed",
        "tip": "Cherries need consistent watering when fruit is developing!",
        "timeframe": "No immediate action needed",
        "success_rate": "100% - Plant is healthy"
    },

    # ==================== CORN DISEASES ====================
    "Gray leaf spot": {
        "name": "Gray Leaf Spot",
        "icon": "🌽",
        "immediate": [
            "Remove infected leaves",
            "Improve air circulation",
            "Avoid overhead watering"
        ],
        "treatment": [
            "Apply fungicide containing azoxystrobin or pyraclostrobin",
            "Treat at first sign of infection",
            "Rotate crops next season"
        ],
        "prevention": [
            "Plant resistant hybrids",
            "Crop rotation (2+ years)",
            "Tillage to bury crop residue",
            "Avoid high nitrogen levels"
        ],
        "organic": "Copper fungicide or neem oil",
        "chemical": "Azoxystrobin or Pyraclostrobin",
        "tip": "Gray leaf spot overwinters in corn residue. Rotate crops!",
        "timeframe": "Treat within 5-7 days",
        "success_rate": "75-80% with early treatment"
    },
    "Common rust": {
        "name": "Common Rust",
        "icon": "🌽",
        "immediate": [
            "Remove infected leaves",
            "Increase air circulation",
            "Avoid overhead watering"
        ],
        "treatment": [
            "Apply azoxystrobin or propiconazole",
            "Treat when rust first appears",
            "Repeat every 7-10 days if needed"
        ],
        "prevention": [
            "Plant resistant varieties",
            "Avoid planting near alternate hosts",
            "Good field sanitation"
        ],
        "organic": "Sulfur or neem oil",
        "chemical": "Azoxystrobin or Propiconazole",
        "tip": "Rust spores spread by wind. Early detection is key!",
        "timeframe": "Treat within 5-7 days",
        "success_rate": "85% with early treatment"
    },
    "Northern leaf blight": {
        "name": "Northern Leaf Blight",
        "icon": "🌽",
        "immediate": [
            "Remove infected leaves immediately",
            "Improve air circulation",
            "Avoid overhead watering"
        ],
        "treatment": [
            "Apply strobilurin or triazole fungicide",
            "Treat at first symptoms",
            "Continue every 7-14 days"
        ],
        "prevention": [
            "Plant resistant hybrids",
            "Crop rotation (2-3 years)",
            "Tillage to bury residue",
            "Balanced fertility"
        ],
        "organic": "Copper fungicide",
        "chemical": "Azoxystrobin or Propiconazole",
        "tip": "Northern leaf blight loves humid conditions. Space plants properly!",
        "timeframe": "Treat within 5-7 days",
        "success_rate": "80% with early treatment"
    },
    "Corn healthy": {
        "name": "Healthy Corn",
        "icon": "🌽✅",
        "immediate": ["Continue good care", "Monitor for pests"],
        "treatment": ["Consistent watering during tasseling", "Balanced fertilization"],
        "prevention": ["Crop rotation", "Plant at proper density", "Good soil fertility"],
        "organic": "Compost and organic fertilizer",
        "chemical": "No treatment needed",
        "tip": "Corn needs consistent water during silking and tasseling!",
        "timeframe": "No immediate action needed",
        "success_rate": "100% - Plant is healthy"
    },

    # ==================== GRAPE DISEASES ====================
    "Grape black rot": {
        "name": "Black Rot",
        "icon": "🍇",
        "immediate": [
            "Remove infected berries and leaves",
            "Prune infected canes 4-6 inches below symptoms",
            "Clean up fallen debris"
        ],
        "treatment": [
            "Apply myclobutanil or captan",
            "Begin at bud break",
            "Continue every 10-14 days"
        ],
        "prevention": [
            "Prune for air circulation",
            "Remove mummified berries",
            "Apply dormant sprays",
            "Plant resistant varieties"
        ],
        "organic": "Copper or sulfur fungicide",
        "chemical": "Myclobutanil or Captan",
        "tip": "Black rot can destroy entire grape crop if untreated!",
        "timeframe": "Treat immediately",
        "success_rate": "80-85% with aggressive treatment"
    },
    "Black measles": {
        "name": "Black Measles (Esca)",
        "icon": "🍇",
        "immediate": [
            "Remove infected wood",
            "Improve vine vigor with proper nutrition",
            "Avoid water stress"
        ],
        "treatment": [
            "No chemical cure available",
            "Prune out dead wood",
            "Maintain vine health",
            "Remove severely infected vines"
        ],
        "prevention": [
            "Use disease-free planting material",
            "Avoid wounding vines",
            "Proper pruning techniques",
            "Maintain vine vigor"
        ],
        "organic": "Compost tea and seaweed extract for vine health",
        "chemical": "No effective chemical treatment",
        "tip": "Esca is a complex trunk disease. Prevention through vine health is key!",
        "timeframe": "Monitor and manage",
        "success_rate": "50-60% - Difficult to control"
    },
    "Leaf blight": {
        "name": "Leaf Blight",
        "icon": "🍇",
        "immediate": [
            "Remove infected leaves",
            "Improve air circulation",
            "Avoid overhead watering"
        ],
        "treatment": [
            "Apply copper or mancozeb fungicide",
            "Treat every 7-10 days",
            "Focus on lower canopy"
        ],
        "prevention": [
            "Prune for good airflow",
            "Remove basal leaves",
            "Avoid wetting foliage",
            "Manage canopy density"
        ],
        "organic": "Copper fungicide",
        "chemical": "Mancozeb or Copper hydroxide",
        "tip": "Leaf blight starts in the lower canopy. Remove lower leaves!",
        "timeframe": "Treat within 5-7 days",
        "success_rate": "85% with early treatment"
    },
    "Grape healthy": {
        "name": "Healthy Grape Vine",
        "icon": "🍇✅",
        "immediate": ["Continue good care", "Monitor for pests"],
        "treatment": ["Proper pruning", "Balanced fertilization", "Regular watering"],
        "prevention": ["Annual dormant pruning", "Canopy management", "Disease monitoring"],
        "organic": "Compost and seaweed extract",
        "chemical": "No treatment needed",
        "tip": "Grapes need proper pruning for good air circulation and fruit production!",
        "timeframe": "No immediate action needed",
        "success_rate": "100% - Plant is healthy"
    },

    # ==================== ORANGE/CITRUS DISEASES ====================
    "Citrus greening": {
        "name": "Citrus Greening (Huanglongbing)",
        "icon": "🍊",
        "immediate": [
            "URGENT: Report to agricultural authorities",
            "Remove infected tree immediately",
            "Control psyllid vectors",
            "Do not move plant material"
        ],
        "treatment": [
            "No cure available - tree must be removed",
            "Control Asian citrus psyllid",
            "Use certified disease-free trees",
            "Apply nutritional sprays to maintain health"
        ],
        "prevention": [
            "Use certified disease-free nursery stock",
            "Control psyllids with insecticides",
            "Remove and destroy infected trees",
            "Plant resistant varieties if available",
            "Regular monitoring"
        ],
        "organic": "Kaolin clay for psyllid control",
        "chemical": "Imidacloprid for psyllid control",
        "tip": "Citrus greening is fatal. Prevention through vector control is critical!",
        "timeframe": "Remove immediately",
        "success_rate": "0% - Tree will die within 3-5 years"
    },

    # ==================== PEACH DISEASES ====================
    "Bacterial spot": {
        "name": "Bacterial Spot",
        "icon": "🍑",
        "immediate": [
            "Remove infected leaves and fruit",
            "Avoid working with plants when wet",
            "Disinfect tools between plants"
        ],
        "treatment": [
            "Apply copper bactericide",
            "Add spreader-sticker for better coverage",
            "Treat every 7-10 days",
            "Stop treatment 2 weeks before harvest"
        ],
        "prevention": [
            "Use disease-free seeds",
            "Rotate crops (3-4 years)",
            "Avoid overhead irrigation",
            "Improve air circulation",
            "Remove plant debris after harvest"
        ],
        "organic": "Copper fungicide/bactericide",
        "chemical": "Copper hydroxide + Mancozeb",
        "tip": "Bacteria spread through water splash. Water carefully at base!",
        "timeframe": "Treat within 3-5 days",
        "success_rate": "70-75% - bacteria are hard to control"
    },
    "Peach healthy": {
        "name": "Healthy Peach Tree",
        "icon": "🍑✅",
        "immediate": ["Continue good care", "Monitor for pests"],
        "treatment": ["Annual pruning", "Balanced fertilization", "Regular watering"],
        "prevention": ["Apply dormant oil in winter", "Thin fruit for size", "Clean up fallen fruit"],
        "organic": "Compost mulch",
        "chemical": "No treatment needed",
        "tip": "Peaches need winter chill hours. Choose varieties for your climate!",
        "timeframe": "No immediate action needed",
        "success_rate": "100% - Plant is healthy"
    },

    # ==================== PEPPER DISEASES ====================
    "Pepper bacterial spot": {
        "name": "Bacterial Spot",
        "icon": "🫑",
        "immediate": [
            "Remove infected leaves",
            "Avoid overhead watering",
            "Disinfect tools"
        ],
        "treatment": [
            "Apply copper bactericide",
            "Treat every 5-7 days",
            "Use resistant varieties next season"
        ],
        "prevention": [
            "Use disease-free seed",
            "Crop rotation (3+ years)",
            "Avoid working when plants wet",
            "Good air circulation"
        ],
        "organic": "Copper spray",
        "chemical": "Copper hydroxide",
        "tip": "Bacterial spot loves warm, wet weather. Water early morning!",
        "timeframe": "Treat within 3-5 days",
        "success_rate": "70-75% with early treatment"
    },
    "Pepper healthy": {
        "name": "Healthy Pepper Plant",
        "icon": "🫑✅",
        "immediate": ["Continue good care", "Monitor for pests"],
        "treatment": ["Consistent watering", "Balanced fertilizer", "Stake for support"],
        "prevention": ["Mulch to retain moisture", "Avoid overwatering", "Space properly"],
        "organic": "Compost tea monthly",
        "chemical": "No treatment needed",
        "tip": "Peppers love heat. Wait until soil warms to plant!",
        "timeframe": "No immediate action needed",
        "success_rate": "100% - Plant is healthy"
    },

    # ==================== POTATO DISEASES ====================
    "Early blight": {
        "name": "Early Blight",
        "icon": "🥔",
        "immediate": [
            "Remove infected lower leaves",
            "Clean up fallen debris around plant",
            "Avoid overhead watering"
        ],
        "treatment": [
            "Apply chlorothalonil or copper fungicide",
            "Treat every 7-10 days",
            "Focus on lower leaves where infection starts"
        ],
        "prevention": [
            "Mulch around plants",
            "Water at base early morning",
            "Stake plants for air circulation",
            "Rotate crops annually"
        ],
        "organic": "Copper fungicide or Bacillus subtilis",
        "chemical": "Chlorothalonil or Azoxystrobin",
        "tip": "Early blight starts on older lower leaves. Remove them early!",
        "timeframe": "Treat within 5-7 days",
        "success_rate": "80-85% with early treatment"
    },
    "Late blight": {
        "name": "Late Blight",
        "icon": "🥔",
        "immediate": [
            "URGENT: Remove and destroy infected plants immediately",
            "Do NOT compost infected material",
            "Bag and dispose in trash",
            "Notify nearby gardeners"
        ],
        "treatment": [
            "Apply copper fungicide as emergency treatment",
            "Use chlorothalonil for severe infections",
            "Apply every 5-7 days in wet weather",
            "Destroy plant if >50% infected"
        ],
        "prevention": [
            "Use certified disease-free seed potatoes",
            "Avoid overhead irrigation",
            "Space plants for good airflow",
            "Monitor weather forecasts (cool, wet conditions favor disease)",
            "Apply preventative fungicides before symptoms"
        ],
        "organic": "Copper fungicide (copper sulfate)",
        "chemical": "Chlorothalonil or Mandipropamid",
        "tip": "Late blight caused the Irish Potato Famine. Take it very seriously!",
        "timeframe": "Treat IMMEDIATELY",
        "success_rate": "60-70% - very aggressive disease"
    },
    "Potato healthy": {
        "name": "Healthy Potato Plant",
        "icon": "🥔✅",
        "immediate": ["Continue good care", "Monitor for pests"],
        "treatment": ["Consistent watering", "Hill soil around stems", "Regular fertilization"],
        "prevention": ["Use certified seed potatoes", "Crop rotation", "Good soil drainage"],
        "organic": "Compost and organic fertilizer",
        "chemical": "No treatment needed",
        "tip": "Hill soil around potato stems to increase yield and prevent greening!",
        "timeframe": "No immediate action needed",
        "success_rate": "100% - Plant is healthy"
    },

    # ==================== RASPBERRY DISEASES ====================
    "Raspberry healthy": {
        "name": "Healthy Raspberry",
        "icon": "🍓✅",
        "immediate": ["Continue good care", "Monitor for pests"],
        "treatment": ["Annual pruning", "Regular watering", "Mulch to retain moisture"],
        "prevention": ["Remove old canes after fruiting", "Good air circulation", "Clean up fallen leaves"],
        "organic": "Compost mulch",
        "chemical": "No treatment needed",
        "tip": "Remove fruited canes immediately after harvest for better production!",
        "timeframe": "No immediate action needed",
        "success_rate": "100% - Plant is healthy"
    },

    # ==================== SOYBEAN DISEASES ====================
    "Soybean healthy": {
        "name": "Healthy Soybean",
        "icon": "🌱✅",
        "immediate": ["Continue good care", "Monitor for pests"],
        "treatment": ["Consistent moisture during pod fill", "Balanced fertility"],
        "prevention": ["Crop rotation", "Inoculate seeds with rhizobium", "Good weed control"],
        "organic": "Compost and organic fertilizer",
        "chemical": "No treatment needed",
        "tip": "Soybeans fix their own nitrogen. Don't over-fertilize!",
        "timeframe": "No immediate action needed",
        "success_rate": "100% - Plant is healthy"
    },

    # ==================== SQUASH DISEASES ====================
    "Squash powdery mildew": {
        "name": "Powdery Mildew",
        "icon": "🎃",
        "immediate": [
            "Remove severely infected leaves",
            "Increase air circulation",
            "Avoid overhead watering"
        ],
        "treatment": [
            "Apply sulfur or potassium bicarbonate",
            "Use baking soda spray",
            "Remove infected leaves promptly"
        ],
        "prevention": [
            "Plant resistant varieties",
            "Space plants for air flow",
            "Water early morning",
            "Remove old plant debris"
        ],
        "organic": "Milk spray (40% milk, 60% water)",
        "chemical": "Sulfur or Potassium bicarbonate",
        "tip": "Powdery mildew loves crowded conditions. Give squash plenty of space!",
        "timeframe": "Treat within 7 days",
        "success_rate": "85-90% with early treatment"
    },

    # ==================== STRAWBERRY DISEASES ====================
    "Leaf scorch": {
        "name": "Leaf Scorch",
        "icon": "🍓",
        "immediate": [
            "Remove infected leaves",
            "Improve air circulation",
            "Reduce overhead watering"
        ],
        "treatment": [
            "Apply copper or sulfur fungicide",
            "Remove old mulch",
            "Apply fresh straw mulch"
        ],
        "prevention": [
            "Plant in well-drained soil",
            "Space plants properly",
            "Remove old leaves in spring",
            "Rotate strawberry beds every 3-4 years"
        ],
        "organic": "Copper fungicide",
        "chemical": "Captan or Sulfur",
        "tip": "Leaf scorch thrives in wet conditions. Keep leaves dry!",
        "timeframe": "Treat within 5-7 days",
        "success_rate": "80% with early treatment"
    },
    "Strawberry healthy": {
        "name": "Healthy Strawberry",
        "icon": "🍓✅",
        "immediate": ["Continue good care", "Monitor for runners"],
        "treatment": ["Regular watering", "Mulch with straw", "Remove old leaves"],
        "prevention": ["Renovate beds after harvest", "Rotate beds every 3-4 years", "Good drainage"],
        "organic": "Compost mulch",
        "chemical": "No treatment needed",
        "tip": "Renovate strawberry beds right after harvest for next year's crop!",
        "timeframe": "No immediate action needed",
        "success_rate": "100% - Plant is healthy"
    },

    # ==================== TOMATO DISEASES ====================
    "Tomato bacterial spot": {
        "name": "Bacterial Spot",
        "icon": "🍅",
        "immediate": [
            "Remove infected leaves",
            "Avoid overhead watering",
            "Disinfect tools between plants"
        ],
        "treatment": [
            "Apply copper bactericide",
            "Treat every 5-7 days",
            "Use resistant varieties next season"
        ],
        "prevention": [
            "Use disease-free seed",
            "Crop rotation (3+ years)",
            "Avoid working plants when wet",
            "Stake for air circulation"
        ],
        "organic": "Copper spray",
        "chemical": "Copper hydroxide",
        "tip": "Bacterial spot spreads rapidly in warm, wet weather!",
        "timeframe": "Treat within 3-5 days",
        "success_rate": "70-75% with early treatment"
    },
    "Tomato early blight": {
        "name": "Early Blight",
        "icon": "🍅",
        "immediate": [
            "Remove infected lower leaves",
            "Clean up fallen debris",
            "Avoid wetting leaves"
        ],
        "treatment": [
            "Apply chlorothalonil or copper",
            "Treat every 7-10 days",
            "Remove infected leaves promptly"
        ],
        "prevention": [
            "Mulch around plants",
            "Water at base",
            "Stake or cage plants",
            "Rotate crops annually"
        ],
        "organic": "Copper fungicide",
        "chemical": "Chlorothalonil",
        "tip": "Early blight starts on lower leaves. Remove bottom leaves early!",
        "timeframe": "Treat within 5-7 days",
        "success_rate": "80-85% with early treatment"
    },
    "Tomato late blight": {
        "name": "Late Blight",
        "icon": "🍅",
        "immediate": [
            "URGENT: Remove infected plants immediately",
            "Bag and dispose in trash",
            "Do NOT compost",
            "Notify nearby gardeners"
        ],
        "treatment": [
            "Apply copper fungicide immediately",
            "Use chlorothalonil for severe cases",
            "Destroy plant if >50% infected"
        ],
        "prevention": [
            "Use resistant varieties",
            "Avoid overhead watering",
            "Good air circulation",
            "Monitor weather for favorable conditions"
        ],
        "organic": "Copper fungicide",
        "chemical": "Chlorothalonil",
        "tip": "Late blight can destroy entire tomato crop in days! Act fast!",
        "timeframe": "Treat IMMEDIATELY",
        "success_rate": "60-70% - very aggressive"
    },
    "Leaf mold": {
        "name": "Leaf Mold",
        "icon": "🍅",
        "immediate": [
            "Remove infected leaves",
            "Increase air circulation",
            "Reduce humidity"
        ],
        "treatment": [
            "Apply copper or sulfur fungicide",
            "Improve ventilation",
            "Reduce nitrogen fertilizer"
        ],
        "prevention": [
            "Space plants adequately",
            "Prune for air flow",
            "Avoid overhead watering",
            "Remove lower leaves"
        ],
        "organic": "Copper spray",
        "chemical": "Chlorothalonil",
        "tip": "Leaf mold thrives in high humidity. Improve air circulation!",
        "timeframe": "Treat within 5-7 days",
        "success_rate": "85% with improved conditions"
    },
    "Septoria leaf spot": {
        "name": "Septoria Leaf Spot",
        "icon": "🍅",
        "immediate": [
            "Remove infected leaves immediately",
            "Clean up fallen debris",
            "Avoid overhead watering"
        ],
        "treatment": [
            "Apply chlorothalonil or copper",
            "Treat every 7-10 days",
            "Focus on lower leaves"
        ],
        "prevention": [
            "Mulch around plants",
            "Water at base",
            "Remove lower leaves",
            "Crop rotation"
        ],
        "organic": "Copper fungicide",
        "chemical": "Chlorothalonil",
        "tip": "Septoria starts on lower leaves. Remove them early for prevention!",
        "timeframe": "Treat within 5-7 days",
        "success_rate": "85% with early treatment"
    },
    "Spider mites": {
        "name": "Spider Mites",
        "icon": "🕷️",
        "immediate": [
            "Spray plants with strong water jet",
            "Isolate infested plants",
            "Remove heavily infested leaves"
        ],
        "treatment": [
            "Apply insecticidal soap",
            "Use neem oil spray",
            "Release predatory mites",
            "Repeat treatment every 5-7 days"
        ],
        "prevention": [
            "Keep plants well-watered (mites hate humidity)",
            "Regularly hose down plants",
            "Avoid broad-spectrum pesticides",
            "Inspect undersides of leaves"
        ],
        "organic": "Insecticidal soap, neem oil, or predatory mites",
        "chemical": "Abamectin or Spiromesifen",
        "tip": "Spider mites thrive in hot, dry conditions. Increase humidity to control them!",
        "timeframe": "Treat within 3-5 days",
        "success_rate": "90% with early treatment"
    },
    "Target spot": {
        "name": "Target Spot",
        "icon": "🍅",
        "immediate": [
            "Remove infected leaves",
            "Improve air circulation",
            "Avoid overhead watering"
        ],
        "treatment": [
            "Apply chlorothalonil or copper",
            "Treat every 7-10 days",
            "Remove infected plant debris"
        ],
        "prevention": [
            "Crop rotation (3+ years)",
            "Avoid overhead irrigation",
            "Good air circulation",
            "Remove crop residue"
        ],
        "organic": "Copper fungicide",
        "chemical": "Chlorothalonil",
        "tip": "Target spot lesions look like bullseyes. Remove infected leaves promptly!",
        "timeframe": "Treat within 5-7 days",
        "success_rate": "80% with early treatment"
    },
    "Tomato yellow leaf curl virus": {
        "name": "Yellow Leaf Curl Virus",
        "icon": "🍅",
        "immediate": [
            "Remove infected plants immediately",
            "Control whitefly vectors",
            "Do not compost infected plants"
        ],
        "treatment": [
            "No cure - remove infected plants",
            "Control whiteflies",
            "Use resistant varieties next season"
        ],
        "prevention": [
            "Use resistant varieties",
            "Control whiteflies with yellow sticky traps",
            "Use row covers for young plants",
            "Remove weed hosts"
        ],
        "organic": "Remove infected plants, control whiteflies with neem oil",
        "chemical": "Insecticides for whitefly control",
        "tip": "Whiteflies transmit this virus. Control whiteflies to prevent spread!",
        "timeframe": "Remove immediately",
        "success_rate": "Prevention only - no cure"
    },
    "Tomato mosaic virus": {
        "name": "Mosaic Virus",
        "icon": "🍅",
        "immediate": [
            "Remove infected plants immediately",
            "Wash hands and tools",
            "Do not compost infected plants"
        ],
        "treatment": [
            "No cure - remove infected plants",
            "Disinfect growing area",
            "Plant resistant varieties"
        ],
        "prevention": [
            "Use virus-free seed",
            "Wash hands after smoking (tobacco mosaic)",
            "Disinfect tools between plants",
            "Control aphids"
        ],
        "organic": "Remove infected plants",
        "chemical": "No chemical control",
        "tip": "Tobacco mosaic virus can survive on tools for years. Disinfect everything!",
        "timeframe": "Remove immediately",
        "success_rate": "Prevention only - 100% fatal"
    },
    "Tomato healthy": {
        "name": "Healthy Tomato Plant",
        "icon": "🍅✅",
        "immediate": ["Continue good care", "Monitor for pests"],
        "treatment": ["Consistent watering", "Regular fertilization", "Prune suckers"],
        "prevention": ["Rotate crops annually", "Mulch to prevent soil splash", "Stake for support"],
        "organic": "Compost tea monthly",
        "chemical": "No treatment needed",
        "tip": "Remove tomato suckers for better air circulation and larger fruit!",
        "timeframe": "No immediate action needed",
        "success_rate": "100% - Plant is healthy"
    },

    # ==================== GENERAL/BACKGROUND ====================
    "Background without leaves": {
        "name": "No Plant Detected",
        "icon": "❌",
        "immediate": [
            "Please upload a clear image of a plant leaf",
            "Ensure the leaf is clearly visible",
            "Use better lighting for the photo"
        ],
        "treatment": [
            "No treatment needed - this is not a plant",
            "Capture a clear image of a plant leaf",
            "Ensure good lighting and focus"
        ],
        "prevention": [
            "Use a plain background for better detection",
            "Hold camera steady when taking photos",
            "Make sure the leaf is centered in frame"
        ],
        "organic": "N/A",
        "chemical": "N/A",
        "tip": "For best results, take photo of a single leaf on plain background!",
        "timeframe": "N/A",
        "success_rate": "N/A"
    }
}

# Disease name mapping for matching
DISEASE_MAPPING = {
    # Apple
    "apple_scab": "Apple scab",
    "apple_black_rot": "Black rot",
    "apple_cedar_apple_rust": "Cedar apple rust",
    "apple_healthy": "Apple healthy",
    
    # Blueberry
    "blueberry_healthy": "Blueberry healthy",
    
    # Cherry
    "cherry_powdery_mildew": "Powdery mildew",
    "cherry_healthy": "Cherry healthy",
    
    # Corn
    "corn_gray_leaf_spot": "Gray leaf spot",
    "corn_common_rust": "Common rust",
    "corn_northern_leaf_blight": "Northern leaf blight",
    "corn_healthy": "Corn healthy",
    
    # Grape
    "grape_black_rot": "Grape black rot",
    "grape_black_measles": "Black measles",
    "grape_leaf_blight": "Leaf blight",
    "grape_healthy": "Grape healthy",
    
    # Orange
    "orange_haunglongbing": "Citrus greening",
    
    # Peach
    "peach_bacterial_spot": "Bacterial spot",
    "peach_healthy": "Peach healthy",
    
    # Pepper
    "pepper_bacterial_spot": "Pepper bacterial spot",
    "pepper_healthy": "Pepper healthy",
    
    # Potato
    "potato_early_blight": "Early blight",
    "potato_late_blight": "Late blight",
    "potato_healthy": "Potato healthy",
    
    # Raspberry
    "raspberry_healthy": "Raspberry healthy",
    
    # Soybean
    "soybean_healthy": "Soybean healthy",
    
    # Squash
    "squash_powdery_mildew": "Squash powdery mildew",
    
    # Strawberry
    "strawberry_leaf_scorch": "Leaf scorch",
    "strawberry_healthy": "Strawberry healthy",
    
    # Tomato
    "tomato_bacterial_spot": "Tomato bacterial spot",
    "tomato_early_blight": "Tomato early blight",
    "tomato_late_blight": "Tomato late blight",
    "tomato_leaf_mold": "Leaf mold",
    "tomato_septoria_leaf_spot": "Septoria leaf spot",
    "tomato_spider_mites": "Spider mites",
    "tomato_target_spot": "Target spot",
    "tomato_yellow_leaf_curl_virus": "Tomato yellow leaf curl virus",
    "tomato_mosaic_virus": "Tomato mosaic virus",
    "tomato_healthy": "Tomato healthy",
}

def get_recommendations(disease_name, severity, plant_type):
    """Get recommendations based on disease name and severity"""
    disease_lower = disease_name.lower().strip()
    
    # Try direct match first
    if disease_lower in DISEASE_RECOMMENDATIONS:
        matched_rec = DISEASE_RECOMMENDATIONS[disease_lower].copy()
    else:
        # Try mapping
        matched_key = None
        for key, mapped_name in DISEASE_MAPPING.items():
            if key in disease_lower or disease_lower in key:
                matched_key = mapped_name
                break
        
        if matched_key and matched_key in DISEASE_RECOMMENDATIONS:
            matched_rec = DISEASE_RECOMMENDATIONS[matched_key].copy()
        else:
            # Try partial matching
            matched_rec = None
            for key in DISEASE_RECOMMENDATIONS:
                if key.lower() in disease_lower or disease_lower in key.lower():
                    matched_rec = DISEASE_RECOMMENDATIONS[key].copy()
                    break
            
            # Default to healthy if no match
            if not matched_rec:
                matched_rec = DISEASE_RECOMMENDATIONS["Tomato healthy"].copy()
    
    # Adjust recommendations based on severity
    if severity > 75:
        matched_rec["immediate"].insert(0, "🚨 CRITICAL SEVERE INFECTION - Take action TODAY!")
        matched_rec["urgency"] = "CRITICAL"
        matched_rec["timeframe"] = "Treat immediately (24-48 hours)"
        matched_rec["success_rate"] = "60-70% - Severe case"
    elif severity > 50:
        matched_rec["immediate"].insert(0, "⚠️ MODERATE TO SEVERE INFECTION - Treat within 2-3 days")
        matched_rec["urgency"] = "HIGH"
        matched_rec["timeframe"] = "Treat within 2-3 days"
        matched_rec["success_rate"] = "75-80% - Moderate case"
    elif severity > 20:
        matched_rec["immediate"].insert(0, "📋 MODERATE INFECTION - Treat within 5-7 days")
        matched_rec["urgency"] = "MEDIUM"
        matched_rec["timeframe"] = "Treat within 5-7 days"
        matched_rec["success_rate"] = "85-90% - Early case"
    else:
        matched_rec["urgency"] = "LOW"
        matched_rec["timeframe"] = "Monitor and treat as needed"
        matched_rec["success_rate"] = "95%+ - Very early detection"
    
    # Add plant-specific tips
    if plant_type and plant_type != "Unknown":
        matched_rec["tip"] = f"For {plant_type}: {matched_rec.get('tip', 'Early detection saves plants!')}"
    
    return matched_rec