 
# 🎓 Official College Management Portal ➔ Wait, Where is the Makeup & Skincare Store?! 🌸💄

> **🔥 Live Demo Link (24 घंटे की खून-पसीना मेहनत का नतीजा):** [Click Here to View the App](https://collage-management-portal.onrender.com)  
> **📋 Report Title:** *College Website / Student Portal* (As per Vartax Training Report, Page 1)  
> **🛍️ Reality:** *Floral Dreams - Ultimate E-Commerce & Skincare Store*  
> **👨‍💻 Fixed & Deployed By:** Manish (Government Polytechnic Rampur) — *जिन्होंने इंस्टीट्यूट द्वारा दी गई सिर्फ अधूरी कोड फाइलों (बिना रनर, बिना सही मॉड्यूल्स और बिना काम करने वाली सेटिंग्स) को अकेले 24 घंटे लगातार जागकर ठीक किया और इस प्रोजेक्ट को क्लाउड पर लाइव किया है!*

---

## 🧐 कड़वी सच्चाई और महा-घोटाला (The Reality Check)

जब समर ट्रेनिंग के नाम पर इंस्टीट्यूट से प्रोजेक्ट रिपोर्ट और कोड मिला, तो उन्होंने कोई लाइव लिंक नहीं दिया था—बस कुछ अधूरी कोड फाइलें और पीडीएफ थमा दी थीं जो लोकल में भी रन नहीं होतीं। न कोई पूरा रनर था, न सही मॉड्यूल्स और न ही काम करने वाली सेटिंग्स! 

अकेले 24 घंटे सिर खपाने, कोडिंग की कमियों को दूर करने और इस **लाइव लिंक (`https://collage-management-portal.onrender.com`)** पर डिप्लॉय करने के बाद जो असलियत सामने आई, वह यह है:
* **होमपेज पर क्या मिला?** कॉलेज का नोटिस बोर्ड नहीं, बल्कि फूलों, लिपस्टिक और ब्यूटी प्रोडक्ट्स की ऑनलाइन दुकान!
* **फीस जमा करने की जगह क्या है?** सीधा **'My Cart'** और **'My Orders'** का शॉपिंग चेकआउट!
* **छात्रों (Students) का क्या हुआ?** कोड के अंदर से छात्रों को गायब करके सबको सीधे **'Customer'** बना दिया गया है!

> *मतलब साफ है भाई—इन्होंने तो रन करने लायक पूरी चीज दी ही नहीं थी, अपनी 24 घंटे की मेहनत के बाद पता चला कि कॉलेज पोर्टल के नाम पर हमें सीधे मेकअप और ब्यूटी प्रोडक्ट्स का ई-कॉमर्स पोर्टल थमाया गया है!* 😂🛒

---

## 📸 Project Screenshots (देख लीजिए सबूत)

**1. Logged-in Menu View (कस्टमर और कार्ट का जिन्न):**  
![App Screenshot 1](images/screenshot1.jpg)

**2. Guest / Public Menu View (लॉगिन और रजिस्टर विकल्प):**  
![App Screenshot 2](images/screenshot2.jpg)

---

## 🎭 Expectation vs. Reality Table

| रिपोर्ट के कागज पर क्या लिखा है? (As per PDF) | इस लाइव प्रोजेक्ट के अंदर असलियत क्या है? |
| :--- | :--- |
| **प्रोजेक्ट का नाम:** कॉलेज वेबसाइट / स्टूडेंट पोर्टल | **असली प्रोजेक्ट:** *Floral Dreams E-Commerce Store* |
| **टेक्नोलॉजी:** PHP, MySQL (पेज 17) | **असली टेक्नोलॉजी:** Python (Django) और शॉपिंग कार्ट डेटाबेस |
| **डेटाबेस:** Student Info, Timetable, Department | **असली डेटाबेस:** `Customer`, `Product`, `Orders`, `ShoppingCart` |

---

## 💀 Copy-Paste Hall of Fame (नाम बदलना भूल गए!)

इस प्रोजेक्ट की महानता का सबूत इसके 70 पन्नों के डॉक्यूमेंट में साफ चमक रहा है, जहाँ कॉपी-पेस्ट करते वक्त वे ये नाम बदलना ही भूल गए:
* `STUDENT_NAME_HERE`
* `college_name_here`  
> *यानी एक ही जेरॉक्स कॉपी पूरी बटालियन के सिर मढ़ दी गई है! कम से कम नाम तो बदल लेते भाई!* 📄💀

---

## 💻 Technical Section & 24-Hours Struggle (तकनीकी कोड की पोल)

बिना किसी सही रनर, अधूरी फाइलों और गायब मॉड्यूल्स वाले इस प्रोजेक्ट को अकेले 24 घंटे लगातार मेहनत करके ठीक करने के बाद जो डेटा स्ट्रक्चर सामने आया, उसका सच यह है:

```python
# Django Models Reality (जहाँ स्टूडेंट की जगह सीधे कस्टमर और ब्यूटी प्रोडक्ट्स हैं)
class Customer(models.Model):  
    name = models.CharField(max_length=50)
    emailaddress = models.EmailField(max_length=50, primary_key=True)

class Product(models.Model):   
    name = models.CharField(max_length=50)
    price = models.IntegerField(default=0)
    image = models.ImageField(upload_to='newproducts/')

```
---

## 🚀 How to Run Locally (अगर अपनी आँखों से चलाना चाहो)

### 1. Clone the repository:
```bash
git clone https://github.com/manishlab-ai/floral-dreams
cd floral-dreams
```

### 2. Install dependencies:
```bash
pip install -r requirements.txt
```

### 3. Run migrations & server:
```bash
python manage.py migrate
python manage.py runserver
```

### 4. Open in browser:
[http://127.0.0.1:8000/](http://127.0.0.1:8000/) *(और देखिए कि कॉलेज के नाम पर ब्यूटी प्रोडक्ट्स कैसे बिक रहे हैं!)*

---

## ☁️ Deployment on Render (24 Hours Hardwork & Fixing)

इन्होंने कोई लाइव लिंक नहीं दिया था; इस प्रोजेक्ट की अधूरी फाइलों, खराब सेटिंग्स और गायब मॉड्यूल्स को ठीक करके इसे Render पर लाइव करने में पूरे 24 घंटे की लगातार खून-पसीना मेहनत लगी है:

* **Build Command:**
```bash
pip install -r requirements.txt && python manage.py migrate && python manage.py collectstatic --noinput
```

* **Start Command:**
```bash
gunicorn floral_dreams_project.wsgi:application --bind 0.0.0.0:\$PORT
```

> “यह रिपॉजिटरी तब तक लाइव रहेगी और सिस्टम की पोल खोलती रहेगी, जब तक हमारी 24 घंटे की मेहनत और इस फर्जीवाड़े का हिसाब नहीं मिल जाता।” 🤡🔥 



