 Vartax Summer Training Project - Audit & Mismatch Report

## 📌 प्रोजेक्ट का संक्षिप्त विवरण (Project Summary)
यह रिपॉजिटरी **Vartax Global Technology Pvt. Ltd.** द्वारा प्रदान की गई 70 पन्नों की प्रोजेक्ट रिपोर्ट (`vartax project report.pdf`) के आधार पर बनाई गई है। 

## 🚨 पाई गई गंभीर विसंगतियाँ (Discrepancies & Issues Found)

### 1. प्रोजेक्ट टाइटल बनाम वास्तविक कोड (Title vs Actual Code Mismatch)
* **रिपोर्ट में दिया गया नाम:** COLLEGE WEBSITE (पेज 1, 12, 16)
* **वास्तविक कोड:** E-Commerce / Online Shopping Store (Floral Dreams - Beauty & Skincare Products)
* **सबूत:** रिपोर्ट के अंदर `models.py` और `views.py` में `Customer`, `Product`, `Orders`, और `ShoppingCart` जैसी ई-कॉमर्स टेबल और लॉजिक हैं।

### 2. टेक्नोलॉजी का विरोधाभास (Technology Mismatch)
* **सॉफ्टवेयर रिक्वायरमेंट्स (पेज 17):** PHP, MySQL
* **सोर्स कोड (पेज 26-38):** Python (Django Framework)

### 3. अधूरा डेटा और प्लेसहोल्डर्स (Placeholders Left)
* रिपोर्ट में कई स्थानों पर `STUDENT_NAME_HERE` और `college_name_here` बिना संपादन के छोड़े गए हैं।

---
*नोट: यह रिपॉजिटरी संस्थान द्वारा दी गई रिपोर्ट की तकनीकी समीक्षा और वाईवा प्रमाण-पत्र हेतु तैयार की गई है।*
h-proof