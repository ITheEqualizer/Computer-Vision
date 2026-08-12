# 🧠 Computer Vision Project | پروژه بینایی ماشین

## 📘 Overview | معرفی
This project is a **Deep Learning-based Computer Vision system** that identifies objects in images using a trained Convolutional Neural Network (CNN). It was developed to demonstrate end-to-end image classification workflows, including data preprocessing, model training, evaluation, and deployment.

این پروژه یک **سیستم بینایی ماشین مبتنی بر یادگیری عمیق** است که قادر است اشیاء موجود در تصاویر را شناسایی کند. این مدل با استفاده از شبکه‌های عصبی کانولوشنی (CNN) آموزش دیده و شامل مراحل آماده‌سازی داده، آموزش مدل، ارزیابی و ذخیره‌سازی خروجی نهایی است.

---

## 📚 Full Documentation (Wiki) | مستندات کامل (ویکی)

A **complete, step-by-step wiki** explaining every line of code — including **all code blocks, English + Persian explanations**, model breakdown, training pipeline, evaluation, and deployment — is available here:

👉 **Visit the Full Wiki:**  
https://github.com/ITheEqualizer/Computer-Vision-CIFAR-10/wiki

🔹 The wiki includes the following full sections:

1. **Setup & Imports**  
2. **Data Loading & Preprocessing**  
3. **Model Architecture**  
4. **Training Configuration & Execution**  
5. **Evaluation, Visualization & Saving**  

📌 *If you want to understand the logic behind every part of the project, the wiki contains the full learning roadmap.*

---

## ⚙️ Features | ویژگی‌ها
- ✅ Image classification using CNN (Keras/TensorFlow)  
- 🧩 Trained model saved as `.keras` and `.h5` files  
- 📊 Evaluation with test data for accuracy & loss metrics  
- 🖼️ Example images included (`img.jpg`, `img2.jpg`)  
- 💾 Supports model loading and reusability  

---

## 📂 Repository Structure | ساختار مخزن
```
Computer-Vision-CIFAR-10/
├── saved_model/
│   ├── cnn_cifar10.keras              # Trained CNN model
│   ├── best_weights.weights.h5        # Saved model weights
├── img.jpg                            # Sample image 1
├── img2.jpg                           # Sample image 2
├── LICENSE                            # License file
├── README.md                          # Readme file
└── .gitignore / .gitattributes        # Git configuration
```

---

## 🧠 Model Architecture | معماری مدل
The model is a **Convolutional Neural Network (CNN)** trained on the CIFAR-10 dataset (or similar custom dataset). It consists of:

- Multiple convolutional and pooling layers  
- Dense fully-connected layers  
- Softmax output for 10-class classification  

این مدل از **شبکه‌های عصبی کانولوشنی (CNN)** برای استخراج ویژگی‌ها و طبقه‌بندی تصاویر استفاده می‌کند و برای مجموعه داده‌ای مشابه CIFAR-10 طراحی شده است. ساختار آن شامل چندین لایه کانولوشن، Pooling و لایه‌های Fully Connected است.

---

## 🚀 Installation & Usage | نصب و اجرا

### 1️⃣ Prerequisites | پیش‌نیازها
Ensure Python 3.8+ is installed and install the following dependencies:
```bash
pip install tensorflow numpy matplotlib
```

### 2️⃣ Run Model | اجرای مدل
To load and test the trained model:
```python
from tensorflow import keras
from tensorflow.keras.preprocessing import image
import numpy as np

class_names = [
    'airplane', 'automobile', 'bird', 'cat', 'deer',
    'dog', 'frog', 'horse', 'ship', 'truck',
]

model = keras.models.load_model('saved_model/cnn_cifar10.keras')

img = image.load_img('img.jpg', target_size=(32, 32), color_mode='rgb')
img_array = image.img_to_array(img)
img_array = np.expand_dims(img_array, axis=0) / 255.0

probabilities = model.predict(img_array, verbose=0)[0]
predicted_index = int(np.argmax(probabilities))
print('Predicted class:', class_names[predicted_index])
print('Confidence:', f'{probabilities[predicted_index]:.2%}')
```

برای اجرای مدل کافی است آن را با استفاده از Keras بارگذاری کرده و تصویر مورد نظر را برای پیش‌بینی وارد کنید.

### 3️⃣ Validate Saved Model | اعتبارسنجی مدل ذخیره‌شده
Verify that the checked-in model still accepts CIFAR-10 image tensors, returns
a valid 10-class probability distribution, and recognizes both sample images:
```bash
python -m unittest discover -s tests -v
```

---

## 📊 Results & Evaluation | نتایج و ارزیابی
The saved notebook records 82.52% accuracy and 0.5162 loss on the 10,000-image CIFAR-10 test set. You can visualize the accuracy/loss graphs or confusion matrix using `matplotlib`.

دفترچهٔ ذخیره‌شده روی ۱۰٬۰۰۰ تصویر آزمایشی CIFAR-10، دقت ۸۲٫۵۲ درصد و خطای ۰٫۵۱۶۲ را ثبت کرده است. برای مشاهده عملکرد می‌توانید از نمودارهای دقت و خطا استفاده کنید.

---

## 🔮 Future Work | کارهای آینده
- Expand dataset for more real-world classes  
- Convert model to TensorFlow Lite for mobile deployment  
- Integrate webcam-based real-time detection  

---

## 📜 License | مجوز
This project is licensed under the MIT License. See the [LICENSE](./LICENSE) file for details.

این پروژه تحت مجوز MIT منتشر شده است. برای اطلاعات بیشتر فایل LICENSE را مطالعه کنید.

---

## 👤 Author | نویسنده
**Developed by:** [ITheEqualizer](https://github.com/ITheEqualizer)

**تهیه و توسعه توسط:** [ITheEqualizer](https://github.com/ITheEqualizer)

---

> 🌍 *A fully bilingual README to help both English and Persian speakers understand and use this project effectively.*  
> 📘 *For full project documentation, visit the wiki!*
