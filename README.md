
<h1>What is Open Receipts ?</h1>
<img src="docs/OpenReceiptsTitle.jpg" width="80%"><br>
Open Receipts is an open source web app to free your food receipts by creating Open Data using text recognition and APIs like Open Food or Open Food Facts.

<img src="docs/SadBasket.png" width="80%">
<img src="docs/HappyBasket.png" width="80%">
<img src="docs/Result.png" width="80%">

<h1>How does it work ?</h1>
<img src="docs/OpenReceiptsHowDoesItWork.jpg" width="80%">

<h1>Features</h1>
<ul>
  <li>Gets the barcodes from a food receipt</li>
  <li>Gets the prices from a food receipt</li>
</ul>

<h1>General Roadmap</h1>
<ul>
<li>Make it translatable</li>
<li>Make it installable (eg Heroku)</li>
</ul>

<h1>Upload Roadmap</h1>
<ul>
  <li>Crowdsourcing matches between abbreviation and barcode</li>
  <li>Getting GPS coordinates for the scan of the receipt</li>
  <li>Bulk upload of receipts</li>
</ul>

<h1>Recognition Roadmap</h1>
  <li>Gets the store from a food receipt</li>
  <li>Gets the timestamp of the purchase from a food receipt</li>
  <li>Gets the location of the purchase store from a food receipt</li>

<h1>Visualisation/Export Roadmap</h1>
<ul>
  <li>Export to CSV</li>
  <li>Reproduce the receipt with CSS</li>
  <li>Repartition of nutrients over time (3 lines)</li>
  <li>Price by calorie (scatter plot)</li>
  <li>Be able to export the anonymized data to a centralized repo</li>
</ul>

# Instructions

1. Get a Google developer account and enable [Cloud Vision API](https://console.cloud.google.com/apis/api/vision.googleapis.com/overview)

2. Generate a credential key and export it to your environment

`export GOOGLE_API_KEY=abcdef`

3. Set up a virtual environment, install via pip, then

`python manage.py migrate`

`python manage.py runserver`
