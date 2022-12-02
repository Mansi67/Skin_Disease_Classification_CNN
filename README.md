# Project: Skin_Disease_Classification_CNN
These project utilizes deep learning algorithms to classify eight classes of skin diseases namely-
C1: Acne, C2: Eczema, C3: Melanoma, C4: Melasma, C5: Psoriasis, C6: Rosacea, C7: Shingles, C8: Urticaria. 

# DataSet:
Data has been collected from Google, Bing Images and DermNet website. There are total 3390 images belonging to 8 classes.
Datset is imbalanced.


![download](https://user-images.githubusercontent.com/105342764/205256480-b041bf76-d3e8-496a-a220-7738fd8e394e.png)

# Model Performance:

| Model Name  | Accuracy on Test Set |
| ------------- | ------------- |
| VGG16 | 58.25%  |
| InceptionV3  | 72.76%  |
| Retraining InceptionV3  | 82.67%  |
| Retraining InceptionResNet | 83.25% |
| Fine Tuning InceptionV3 (layer >249 trainable=True)| 84.20% |
| Fine Tuning InceptionResNet (layer >600 trainable=True)| 85.26% |

