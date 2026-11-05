Plant Disease Detection 🌿🔍
Building AI course project

Summary
This project is a web application and dashboard designed to detect and classify plant diseases using deep learning. It allows users to upload images of plant leaves to quickly identify potential diseases, utilizing a trained Keras model for inference.

Background
Plant diseases significantly impact global food security and agricultural productivity. Early and accurate detection of these diseases is crucial for preventing widespread crop loss and minimizing the excessive use of chemical pesticides. This project aims to provide farmers and agricultural hobbyists with an accessible tool to identify plant health issues quickly through automated image analysis.

How is it used?
The solution is designed for anyone managing plants, from large-scale farmers to home gardeners. Users access a responsive web application where they can upload an image of a plant leaf. The system processes the image and returns a classification indicating the likely disease. An integrated dashboard is also available for monitoring classification insights and managing data.

Data sources and AI methods
The core of this project is a deep learning model built with Python and Keras (.keras). The model is trained on a dataset of healthy and diseased plant leaf images, utilizing deep learning techniques to extract visual features and classify the diseases. The frontend is built using HTML5, CSS3, and JavaScript to interface with the backend inference engine.

Challenges
The current model's accuracy heavily depends on the quality of the uploaded images. Poor lighting, blurry photos, or obscured leaves can lead to incorrect classifications. Furthermore, the model is limited to the specific diseases it was trained on and may struggle with rare conditions, multiple concurrent diseases, or identifying completely novel pathogens not present in the original dataset.

What next?
Future developments could include:

Expanding the model's training dataset to recognize a wider variety of plant species and diseases.

Developing a dedicated mobile application for easier on-the-field image capture and offline inference.

Integrating treatment recommendations and agricultural guidance based on the detected disease.

Acknowledgments
Built using Python, Keras, and standard web technologies.

Project structure and concept inspired by the Building AI course project template.
