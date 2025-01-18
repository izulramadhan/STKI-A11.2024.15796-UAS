{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Pengumpulan Data Pasien\n",
    "Mengumpulkan data pasien dengan contoh data dummy."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "\n",
    "# Membaca data dari file Excel\n",
    "data_pasien = pd.read_excel('patient_icd_10_rs_sbs.xlsx')\n",
    "\n",
    "# Membuat DataFrame dari data\n",
    "df_pasien = pd.DataFrame(data_pasien)\n",
    "\n",
    "# Menampilkan DataFrame\n",
    "df_pasien"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Pra-pemrosesan Data dan Feature Engineering\n",
    "Melakukan pra-pemrosesan data dan feature engineering untuk persiapan analisis lebih lanjut."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Mengubah nama kolom untuk konsistensi\n",
    "df_pasien.rename(columns={'ID_Pasien': 'id_pasien', 'Nama': 'nama', 'Umur': 'umur', 'Jenis_Kelamin': 'jenis_kelamin', 'Diagnosa_ICD10': 'diagnosa_icd10'}, inplace=True)\n",
    "\n",
    "# Mengubah kolom 'jenis_kelamin' menjadi numerik\n",
    "df_pasien['jenis_kelamin'] = df_pasien['jenis_kelamin'].map({'Laki-laki': 1, 'Perempuan': 0})\n",
    "\n",
    "# Menambahkan kolom 'umur_kategori' berdasarkan rentang umur\n",
    "bins = [0, 18, 35, 50, 65, 100]\n",
    "labels = ['Anak-anak', 'Dewasa Muda', 'Dewasa', 'Paruh Baya', 'Lansia']\n",
    "df_pasien['umur_kategori'] = pd.cut(df_pasien['umur'], bins=bins, labels=labels, right=False)\n",
    "\n",
    "# Menampilkan DataFrame setelah pra-pemrosesan\n",
    "df_pasien"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Eksplorasi dan Analisis Data Awal (EDA)\n",
    "Melakukan eksplorasi dan analisis data awal dengan berbagai bagan."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "import matplotlib.pyplot as plt\n",
    "import seaborn as sns\n",
    "\n",
    "# Melakukan statistik deskriptif untuk data pasien\n",
    "statistik_deskriptif = df_pasien.describe(include='all')\n",
    "print(statistik_deskriptif)\n",
    "\n",
    "# Membuat visualisasi distribusi umur pasien\n",
    "plt.figure(figsize=(10, 6))\n",
    "sns.histplot(df_pasien['umur'], bins=10, kde=True)\n",
    "plt.title('Distribusi Umur Pasien')\n",
    "plt.xlabel('Umur')\n",
    "plt.ylabel('Frekuensi')\n",
    "plt.show()\n",
    "\n",
    "# Mengidentifikasi gejala teratas yang sering dilaporkan\n",
    "gejala_teratas = df_pasien['diagnosa_icd10'].value_counts().head(10)\n",
    "plt.figure(figsize=(10, 6))\n",
    "sns.barplot(x=gejala_teratas.index, y=gejala_teratas.values)\n",
    "plt.title('Gejala Teratas yang Sering Dilaporkan')\n",
    "plt.xlabel('Kode ICD-10')\n",
    "plt.ylabel('Frekuensi')\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Statistik Deskriptif untuk Data Pasien\n",
    "Melakukan statistik deskriptif untuk data pasien."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "import matplotlib.pyplot as plt\n",
    "import seaborn as sns\n",
    "\n",
    "# Melakukan statistik deskriptif untuk data pasien\n",
    "statistik_deskriptif = df_pasien.describe(include='all')\n",
    "print(statistik_deskriptif)\n",
    "\n",
    "# Membuat visualisasi distribusi umur pasien\n",
    "plt.figure(figsize=(10, 6))\n",
    "sns.histplot(df_pasien['umur'], bins=10, kde=True)\n",
    "plt.title('Distribusi Umur Pasien')\n",
    "plt.xlabel('Umur')\n",
    "plt.ylabel('Frekuensi')\n",
    "plt.show()\n",
    "\n",
    "# Mengidentifikasi gejala teratas yang sering dilaporkan\n",
    "gejala_teratas = df_pasien['diagnosa_icd10'].value_counts().head(10)\n",
    "plt.figure(figsize=(10, 6))\n",
    "sns.barplot(x=gejala_teratas.index, y=gejala_teratas.values)\n",
    "plt.title('Gejala Teratas yang Sering Dilaporkan')\n",
    "plt.xlabel('Kode ICD-10')\n",
    "plt.ylabel('Frekuensi')\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Visualisasi Distribusi Umur Pasien\n",
    "Membuat visualisasi distribusi umur pasien."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "import matplotlib.pyplot as plt\n",
    "import seaborn as sns\n",
    "\n",
    "# Membuat visualisasi distribusi umur pasien\n",
    "plt.figure(figsize=(10, 6))\n",
    "sns.histplot(df_pasien['umur'], bins=10, kde=True)\n",
    "plt.title('Distribusi Umur Pasien')\n",
    "plt.xlabel('Umur')\n",
    "plt.ylabel('Frekuensi')\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Identifikasi Gejala Teratas yang Sering Dilaporkan\n",
    "Mengidentifikasi gejala teratas yang sering dilaporkan."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "import matplotlib.pyplot as plt\n",
    "import seaborn as sns\n",
    "\n",
    "# Mengidentifikasi gejala teratas yang sering dilaporkan\n",
    "gejala_teratas = df_pasien['diagnosa_icd10'].value_counts().head(10)\n",
    "\n",
    "# Membuat visualisasi gejala teratas yang sering dilaporkan\n",
    "plt.figure(figsize=(10, 6))\n",
    "sns.barplot(x=gejala_teratas.index, y=gejala_teratas.values)\n",
    "plt.title('Gejala Teratas yang Sering Dilaporkan')\n",
    "plt.xlabel('Kode ICD-10')\n",
    "plt.ylabel('Frekuensi')\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Klasifikasi dengan Naive Bayes\n",
    "Melakukan klasifikasi dengan Naive Bayes."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "from sklearn.model_selection import train_test_split\n",
    "from sklearn.naive_bayes import GaussianNB\n",
    "from sklearn.metrics import classification_report, accuracy_score\n",
    "\n",
    "# Pastikan df_pasien sudah didefinisikan\n",
    "# df_pasien = pd.read_csv('path_to_your_data.csv')\n",
    "\n",
    "# Memisahkan fitur dan label\n",
    "X = df_pasien[['umur', 'jenis_kelamin']]\n",
    "y = df_pasien['diagnosa_icd10']\n",
    "\n",
    "# Memastikan tidak ada nilai yang hilang\n",
    "X = X.dropna()\n",
    "y = y[X.index]\n",
    "\n",
    "# Periksa distribusi label\n",
    "print(\"Distribusi label dalam data:\")\n",
    "print(y.value_counts())\n",
    "\n",
    "# Membagi data menjadi data latih dan data uji\n",
    "X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)\n",
    "\n",
    "# Inisialisasi model Naive Bayes\n",
    "nb_model = GaussianNB()\n",
    "\n",
    "# Melatih model dengan data latih\n",
    "nb_model.fit(X_train, y_train)\n",
    "\n",
    "# Memprediksi label untuk data uji\n",
    "y_pred = nb_model.predict(X_test)\n",
    "\n",
    "# Evaluasi model\n",
    "print(\"Classification Report:\")\n",
    "print(classification_report(y_test, y_pred, zero_division=0))\n",
    "\n",
    "print(\"Accuracy Score:\")\n",
    "print(accuracy_score(y_test, y_pred))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Klasifikasi Decision Tree\n",
    "Melakukan klasifikasi dengan Decision Tree."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "from sklearn.tree import DecisionTreeClassifier\n",
    "from sklearn.metrics import classification_report, accuracy_score, ConfusionMatrixDisplay\n",
    "import matplotlib.pyplot as plt\n",
    "\n",
    "# Inisialisasi model Decision Tree\n",
    "dt_model = DecisionTreeClassifier(random_state=42)\n",
    "\n",
    "# Melatih model dengan data latih\n",
    "dt_model.fit(X_train, y_train)\n",
    "\n",
    "# Memprediksi label untuk data uji\n",
    "y_pred_dt = dt_model.predict(X_test)\n",
    "\n",
    "# Evaluasi model\n",
    "print(\"Classification Report Decision Tree:\")\n",
    "print(classification_report(y_test, y_pred_dt, zero_division=0))\n",
    "\n",
    "print(\"Accuracy Score Decision Tree:\")\n",
    "print(accuracy_score(y_test, y_pred_dt))\n",
    "\n",
    "# Plot confusion matrix\n",
    "plt.figure(figsize=(10, 6))\n",
    "ConfusionMatrixDisplay.from_predictions(\n",
    "    y_test,\n",
    "    y_pred_dt,\n",
    "    cmap=plt.cm.Blues\n",
    ")\n",
    "plt.title('Confusion Matrix Decision Tree')\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Pelatihan Model Machine Learning untuk Klasifikasi ICD-10\n",
    "Melatih model machine learning untuk klasifikasi ICD-10."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "from sklearn.cluster import KMeans\n",
    "from sklearn.preprocessing import StandardScaler\n",
    "from mlxtend.frequent_patterns import apriori, association_rules\n",
    "from sklearn.metrics import classification_report, accuracy_score, ConfusionMatrixDisplay\n",
    "import matplotlib.pyplot as plt\n",
    "import seaborn as sns\n",
    "\n",
    "# Standarisasi fitur\n",
    "scaler = StandardScaler()\n",
    "X_scaled = scaler.fit_transform(X)\n",
    "\n",
    "# Inisialisasi model KMeans\n",
    "kmeans = KMeans(n_clusters=3, random_state=42)\n",
    "\n",
    "# Melatih model KMeans\n",
    "kmeans.fit(X_scaled)\n",
    "\n",
    "# Menambahkan label klaster ke DataFrame\n",
    "df_pasien['klaster'] = kmeans.labels_\n",
    "\n",
    "# Menampilkan DataFrame dengan klaster\n",
    "print(df_pasien)\n",
    "\n",
    "# Membuat visualisasi klaster\n",
    "plt.figure(figsize=(10, 6))\n",
    "sns.scatterplot(x='umur', y='jenis_kelamin', hue='klaster', data=df_pasien, palette='viridis')\n",
    "plt.title('Klaster Pasien Berdasarkan Umur dan Jenis Kelamin')\n",
    "plt.xlabel('Umur')\n",
    "plt.ylabel('Jenis Kelamin')\n",
    "plt.show()\n",
    "\n",
    "# Menggunakan Apriori untuk menemukan aturan asosiasi\n",
    "# Mengubah data menjadi format one-hot encoding\n",
    "df_onehot = pd.get_dummies(df_pasien[['diagnosa_icd10', 'klaster']], columns=['diagnosa_icd10', 'klaster'])\n",
    "\n",
    "# Menjalankan algoritma Apriori\n",
    "frequent_itemsets = apriori(df_onehot, min_support=0.1, use_colnames=True)\n",
    "\n",
    "# Menemukan aturan asosiasi\n",
    "rules = association_rules(frequent_itemsets, metric=\"lift\", min_threshold=1)\n",
    "\n",
    "# Menampilkan aturan asosiasi\n",
    "print(rules)\n",
    "\n",
    "# Evaluasi model Naive Bayes\n",
    "print(\"Classification Report Naive Bayes:\")\n",
    "print(classification_report(y_test, y_pred, zero_division=0))\n",
    "\n",
    "print(\"Accuracy Score Naive Bayes:\")\n",
    "print(accuracy_score(y_test, y_pred))\n",
    "\n",
    "# Evaluasi model Decision Tree\n",
    "print(\"Classification Report Decision Tree:\")\n",
    "print(classification_report(y_test, y_pred_dt, zero_division=0))\n",
    "\n",
    "print(\"Accuracy Score Decision Tree:\")\n",
    "print(accuracy_score(y_test, y_pred_dt))\n",
    "\n",
    "# Plot confusion matrix Decision Tree\n",
    "plt.figure(figsize=(10, 6))\n",
    "ConfusionMatrixDisplay.from_predictions(\n",
    "    y_test,\n",
    "    y_pred_dt,\n",
    "    cmap=plt.cm.Blues\n",
    ")\n",
    "plt.title('Confusion Matrix Decision Tree')\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Klastering\n",
    "Melakukan klastering pada data pasien."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "from sklearn.cluster import KMeans\n",
    "from sklearn.preprocessing import StandardScaler\n",
    "\n",
    "# Standarisasi fitur\n",
    "scaler = StandardScaler()\n",
    "X_scaled = scaler.fit_transform(df_pasien[['umur', 'jenis_kelamin']])\n",
    "\n",
    "# Inisialisasi model KMeans\n",
    "kmeans = KMeans(n_clusters=3, random_state=42)\n",
    "\n",
    "# Melatih model KMeans\n",
    "kmeans.fit(X_scaled)\n",
    "\n",
    "# Menambahkan label klaster ke DataFrame\n",
    "df_pasien['klaster'] = kmeans.labels_\n",
    "\n",
    "# Menampilkan DataFrame dengan klaster\n",
    "print(df_pasien)\n",
    "\n",
    "# Membuat visualisasi klaster\n",
    "plt.figure(figsize=(10, 6))\n",
    "sns.scatterplot(x='umur', y='jenis_kelamin', hue='klaster', data=df_pasien, palette='viridis')\n",
    "plt.title('Klaster Pasien Berdasarkan Umur dan Jenis Kelamin')\n",
    "plt.xlabel('Umur')\n",
    "plt.ylabel('Jenis Kelamin')\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Asosiasi dengan Apriori\n",
    "Melakukan asosiasi dengan algoritma Apriori."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "from mlxtend.frequent_patterns import apriori, association_rules\n",
    "\n",
    "# Menggunakan Apriori untuk menemukan aturan asosiasi\n",
    "# Mengubah data menjadi format one-hot encoding\n",
    "df_onehot = pd.get_dummies(df_pasien[['diagnosa_icd10', 'klaster']], columns=['diagnosa_icd10', 'klaster'])\n",
    "\n",
    "# Menjalankan algoritma Apriori\n",
    "frequent_itemsets = apriori(df_onehot, min_support=0.1, use_colnames=True)\n",
    "\n",
    "# Menemukan aturan asosiasi\n",
    "rules = association_rules(frequent_itemsets, metric=\"lift\", min_threshold=1)\n",
    "\n",
    "# Menampilkan aturan asosiasi\n",
    "print(rules)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Evaluasi Model dan Interpretasi Hasil\n",
    "Melakukan evaluasi model dan interpretasi hasil dengan berbagai bagan."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "import matplotlib.pyplot as plt\n",
    "import seaborn as sns\n",
    "from sklearn.metrics import classification_report, accuracy_score, ConfusionMatrixDisplay\n",
    "\n",
    "# Evaluasi model Naive Bayes\n",
    "print(\"Classification Report Naive Bayes:\")\n",
    "print(classification_report(y_test, y_pred, zero_division=0))\n",
    "\n",
    "print(\"Accuracy Score Naive Bayes:\")\n",
    "print(accuracy_score(y_test, y_pred))\n",
    "\n",
    "# Plot confusion matrix Naive Bayes\n",
    "plt.figure(figsize=(10, 6))\n",
    "ConfusionMatrixDisplay.from_predictions(\n",
    "    y_test,\n",
    "    y_pred,\n",
    "    cmap=plt.cm.Blues\n",
    ")\n",
    "plt.title('Confusion Matrix Naive Bayes')\n",
    "plt.show()\n",
    "\n",
    "# Evaluasi model Decision Tree\n",
    "print(\"Classification Report Decision Tree:\")\n",
    "print(classification_report(y_test, y_pred_dt, zero_division=0))\n",
    "\n",
    "print(\"Accuracy Score Decision Tree:\")\n",
    "print(accuracy_score(y_test, y_pred_dt))\n",
    "\n",
    "# Plot confusion matrix Decision Tree\n",
    "plt.figure(figsize=(10, 6))\n",
    "ConfusionMatrixDisplay.from_predictions(\n",
    "    y_test,\n",
    "    y_pred_dt,\n",
    "    cmap=plt.cm.Blues\n",
    ")\n",
    "plt.title('Confusion Matrix Decision Tree')\n",
    "plt.show()\n",
    "\n",
    "# Membuat visualisasi perbandingan akurasi model\n",
    "akurasi_models = {\n",
    "    'Naive Bayes': accuracy_score(y_test, y_pred),\n",
    "    'Decision Tree': accuracy_score(y_test, y_pred_dt)\n",
    "}\n",
    "\n",
    "plt.figure(figsize=(10, 6))\n",
    "sns.barplot(x=list(akurasi_models.keys()), y=list(akurasi_models.values()))\n",
    "plt.title('Perbandingan Akurasi Model')\n",
    "plt.xlabel('Model')\n",
    "plt.ylabel('Akurasi')\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Penyajian Kesimpulan dan Rekomendasi\n",
    "Menyajikan kesimpulan dan rekomendasi berdasarkan analisis."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Menyajikan Kesimpulan dan Rekomendasi\n",
    "\n",
    "# Kesimpulan\n",
    "kesimpulan = \"\"\"\n",
    "Berdasarkan analisis yang telah dilakukan, berikut adalah beberapa kesimpulan yang dapat diambil:\n",
    "1. Distribusi umur pasien menunjukkan bahwa sebagian besar pasien berada dalam rentang usia dewasa muda dan dewasa.\n",
    "2. Gejala teratas yang sering dilaporkan berdasarkan kode ICD-10.\n",
    "3. Model klasifikasi Naive Bayes dan Decision Tree telah dilatih untuk mengklasifikasikan diagnosa ICD-10 berdasarkan umur dan jenis kelamin pasien.\n",
    "4. Model Decision Tree menunjukkan akurasi yang lebih tinggi dibandingkan dengan model Naive Bayes.\n",
    "5. Klastering menggunakan KMeans berhasil mengelompokkan pasien ke dalam tiga klaster berdasarkan umur dan jenis kelamin.\n",
    "6. Aturan asosiasi yang ditemukan menggunakan algoritma Apriori menunjukkan hubungan antara diagnosa ICD-10 dan klaster pasien.\n",
    "\"\"\"\n",
    "\n",
    "print(kesimpulan)\n",
    "\n",
    "# Rekomendasi\n",
    "rekomendasi = \"\"\"\n",
    "Berdasarkan kesimpulan di atas, berikut adalah beberapa rekomendasi yang dapat diberikan:\n",
    "1. Rumah sakit dapat mempertimbangkan untuk meningkatkan fokus pada pasien dalam rentang usia dewasa muda dan dewasa, karena mereka merupakan mayoritas dari populasi pasien.\n",
    "2. Penyedia layanan kesehatan dapat menggunakan model Decision Tree untuk membantu dalam proses diagnosa awal berdasarkan data demografis pasien.\n",
    "3. Klastering pasien dapat digunakan untuk mengidentifikasi kelompok pasien dengan karakteristik serupa, yang dapat membantu dalam perencanaan perawatan dan sumber daya.\n",
    "4. Aturan asosiasi yang ditemukan dapat digunakan untuk mengidentifikasi pola umum dalam diagnosa pasien, yang dapat membantu dalam pengembangan program pencegahan dan intervensi.\n",
    "\"\"\"\n",
    "\n",
    "print(rekomendasi)\n",
    "\n",
    "# Visualisasi Kesimpulan dan Rekomendasi\n",
    "plt.figure(figsize=(10, 6))\n",
    "sns.barplot(x=list(akurasi_models.keys()), y=list(akurasi_models.values()))\n",
    "plt.title('Perbandingan Akurasi Model')\n",
    "plt.xlabel('Model')\n",
    "plt.ylabel('Akurasi')\n",
    "plt.show()"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.10.12"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
