# Hate Speech Detection
The main aim of this project is to classify tweets in three classes:<br>
  (1) Hate Speech<br>
  (2) Offensive Language<br>
  (3) No Hate speech No offensive language<br><br>
# Dataset
You can download dataset from <a href='https://github.com/AdarshPal740/Twitter-Hate-Speech-Analysis-Against-Women/blob/master/twitter.csv'>this</a> link. This dataset contains 24783 rows and  7 columns.
# dataset understanding
 <b>Top 20 most frequent words per label<b>
  <img src="/visualization/frequent_words.png"><br>
  <p><b>Most popular hashtags of each tweet type<b></p>
  <img src="/visualization/hastag.png"><br>
    <h1> Requirements</h1>
    (1) Pandas<br>
    (2) Numpy<br>
    (3) Scikit-learn<br>
    (4) Matplot<br>
    (5) Nltk
<h1>Model Deployment</h1> 
    I deployed this model using streamlit library.
    <img src="/visualization/final.png">
<br>
    <h1>Conclusion</h1>
    <br>
   <b> The final model's performance is indicative of the two major roadblocks of the project:<b><br><br>
    (1) The massive class imbalance of the dataset.<br>
    (2) The model's inability to "unerstand" the nuances of hate speech.<br><br>
The issue of class imbalance is manageable with preprocessing techniques and oversampling/undersampling techniques. However, identifying hate speech is an overall problem that many major tech companies like Twitter, Facebook and Instagram are still struggling with.
  
  
  
