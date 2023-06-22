# Mildew Detection in Cherry Leaves

## Dataset Content

The main contents of the dataset are disussed in this section.

- The dataset is taken from [Kaggle](https://www.kaggle.com/codeinstitute/cherry-leaves), and it is provided by Code Institute for the purpose of this portfolio project. I have created a fictitious user story where predictive analytics can be applied in a real project in the workplace.
- The dataset contains more than 4 thousand images taken from the client's crop fields. About 50% of the images show healthy cherry leaves and 50% of the images show the cherry leaves containing powdery mildew. Powdery mildew a fungal disease that affects many plant species. The cherry plantation crop is one of the finest products in their portfolio; therefore, the company is concerned about supplying the market with a compromised quality product.

## Business Requirements

The cherry plantation crop from Farmy & Foods is facing a challenge where their cherry plantations have been presenting powdery mildew. Currently, the process is manual verification if a given cherry tree contains powdery mildew. An employee spends around 30 minutes in each tree, taking a few samples of tree leaves and verifying visually if the leaf tree is healthy or has powdery mildew. If there is powdery mildew, the employee applies a specific compound to kill the fungus. The time spent applying this compound is 1 minute. The company has thousands of cherry trees, located on multiple farms across the country. As a result, this manual process is not scalable due to the time spent in the manual process inspection.

To save time in this process, the IT team suggested an ML system that detects instantly, using a leaf tree image, if it is healthy or has powdery mildew. A similar manual process is in place for other crops for detecting pests, and if this initiative is successful, there is a realistic chance to replicate this project for all other crops. The dataset is a collection of cherry leaf images provided by Farmy & Foods, taken from their crops.

The business requirements are:<br>
1 - The client is interested in conducting a study to visually differentiate a cherry leaf that is healthy from one that contains
powdery mildew.<br>
2 - The client is interested in predicting if a cherry tree is healthy or contains powdery mildew.

## Hypothesis and how to validate?

In this section are project hypotheses and the methods to validate them.<br>
1- I suggest that images of cherry leaves with powdery mildew will have enough differences compared to those without the disease in order to train the model with an image dataset.

- The dataset will be analysed, using test, train, and validation techniques to investigate the accuracy of image identification.

2- Based on the company analysis, the manual evaluation of a cherry tree takes 30 minutes for only a few samples of tree leaves to verify that the leaf tree is healthy or has powdery mildew. This study will not only be beneficial for the comapany to reduce the time required to visualize the disease, but also ensure that the detection of mildew is scalable.

- An average image study can help to investigate it.
- The detailed validation process will be displayed in the dashboad.

3- The sample dataset contains images classified as infected and uninfected leaves.

- The binary classification will be the best way to determine the difference between infected and uninftected leaves.
- Upload of images to determine infection will be included in the dashboard.

## The rationale to map the business requirements to the Data Visualisations and ML tasks

The business requirements of the project and a rationale to map them to the Data Visualisations and ML tasks are provided below.

- **Business Requirement 1**: Data Visualization

  - I will display the "mean" and "standard deviation" images for infected and uninfected leaves.
  - I will display the difference between an average infected leaf and an average uninfected leaf.
  - I will display an image montage for either infected or uninfected leaves.

- **Business Requirement 2**: Classification
  - I want to predict if a given leaf is infected or not with powdery mildew.
  - I want to build a binary classifier and generate reports.

## ML Business Case

- I want a ML model to predict if a leaf is infected with powdery mildew or not, based on historical image data. It is a supervised model, a 2-class, single-label, classification model.
- My ideal outcome is provide the Farmy foods team a faster method of determining if a plant is infected with powdery mildew or not.
- The model success metrics are:
  - Accuracy of 65% or above on the test set.
- The model output is defined as a flag, indicating if the leaf is infected with powdery mildew or not and the associated probability of being infected or not. The Farmy foods staff will do the inspection of the leaf as usual and upload the picture to the App. The prediction is made on the fly (not in batches).
- **Heuristics:** Currently, the process is to manually verify if a given cherry tree contains powdery mildew or not. An employee spends around 30 minutes in each tree, taking a few samples of tree leaves and verifying visually if the leaf tree is healthy or has powdery mildew. Although the staff require some training to detect the occurrance of disease in detail, the image analysis, sample collection and processing will be faster and could be performed by staff with less expertise.
- The training data to fit the model come from [Kaggle](https://www.kaggle.com/codeinstitute/cherry-leaves). This dataset contains about 4+ thousand images.
  - Train data - target: infected or not; features: all images.

## Dashboard Design (Streamlit App User Interface)
The dashboard will be consisted five pages provided below.

### Page 1: Project Summary
**Project summary**
This page will provide general information about the project, dataset used for data visualization and prediction, link for the additional information, and business requirements.
- **General Information**
  - Powdery Mildew is a fungal disease infecting herbaceous and woody plants, and can result in a low fruit yield in the case of Cherry Trees.
  - Currently, the process is to manually verify if a given cherry tree contains powdery mildew or not. An employee spends around 30 minutes in each tree, taking a few samples of tree leaves and verifying visually if the leaf tree is healthy or contains powdery mildew.
  - According to the Conneticut Portal, powdery mildews are easily recognized by the white, powdery growth of the fungus on infected portions of the plant host. The powdery appearance results from the superficial growth of the fungus as thread-like strands (hyphae) over the plant surface and the production of chains of spores (conidia). Colonies vary in appearance from fluffy and white to sparse and gray.
- **Project Dataset**
  - The available dataset contains +4 thousand images of cherry leaves taken from the client's crop fields:
  - 2104 images of cherry leaves which are healthy
  - 2104 images of cherry leaves containing powdery mildew
  - For additional information about the data, please visit [Dataset](https://www.kaggle.com/datasets/codeinstitute/cherry-leaves)
- **Link to additional information**
  - Link will be provided for the additional information about the project.
- **Business requirements**
    The project has two business requirements:<br>
    - The client is interested in conducting a study to visually differentiate a cherry leaf that is healthy from one that contains powdery mildew.
    - The client is interested in predicting if a cherry leaf is healthy or contains powdery mildew.

### Page 2: Leaf Visualiser
This page will provide the details for the answer to business requirement 1.<br>
  - Checkbox 1 - Difference between average and variability image
  - Checkbox 2 - Differences between average infected and average uninfected leaves.
  - Checkbox 3 - Image Montage

### Page 3: Mildew Detection
This page will provide information about business requirement 2- "The client is interested in predicting if a cherry leaf is healthy or contains powdery mildew."<br>
- Link to download a set of infected and uninfected leaves for live prediction.
- User Interface with a file uploader widget. The user should upload multiple leaf sample images. It will display the image and a prediction statement, indicating if the leaf is infected or not with powdery mildew and the probability associated with this statement.
- Table with image name and prediction results.
- Download button to download table.

### Page 4: Project Hypothesis and Validation

This page will describe project hypotheses, conclusion and methods used to validate the hypothesis.

### Page 5: ML Performance Metrics
This page will provide the details for the answer to business requirement 2.<br>
- Label Frequencies for Train, Validation and Test Sets
- Model History - Accuracy and Losses
- Model evaluation result

## Unfixed Bugs
* No unfixed bugs.

## Deployment

### Heroku

- The App live link is: https://YOUR_APP_NAME.herokuapp.com/
- The project was deployed to Heroku using the following steps.

1. Log in to Heroku and create an App
2. At the Deploy tab, select GitHub as the deployment method.
3. Select your repository name and click Search. Once it is found, click Connect.
4. Select the branch you want to deploy, then click Deploy Branch.
5. The deployment process should happen smoothly if all deployment files are fully functional. Click now the button Open App on the top of the page to access your App.

The Battleships Game was deployed using Code Institute's mock terminal for Heroku.
The steps for deployment were as follows:
* Fork or clone this repository
* Create a new Heroku app
* Set the buildpacks to Python and NodeJS in that order
* Link the Heroku app to the repository
* Click on Deploy

## Main Data Analysis and Machine Learning Libraries

- Here you should list the libraries used in the project and provide an example(s) of how you used these libraries.

## Credits
To complete the contents of Mildew detection in Cherry leaves, I learned coding and collected the information from different sources.
- Learned Python coding from [Code Institute](https://learn.codeinstitute.net/)
- Used Code Institute student template [template](Code-Institute-Solutions/milestone-project-mildew-detection-in-cherry-leaves)
- Collected information on good and bad coding practices from:
  - [Documenting Python Code](https://realpython.com/documenting-python-code/)
- The description on the malaria detection in blood cells provided by the tutor of the Code Institute with [Malaria Detection](Code-Institute-Solutions/WalkthroughProject01) and app [Malaria Detector](https://malaria-predictor.onrender.com/) was useful as well as an inspiration to design [Image Identification](https://github.com/HumaIlyas/mildew-detection-image-identification).

[Back to Table of contents](#table-of-contents)

### Content
- The leaf icons in the dashboard.py filw was taken from [Font Awesome](https://fontawesome.com/).
- The details about the powdery mildew  were found at [Conneticut Portal](https://portal.ct.gov/CAES/Fact-Sheets/Plant-Pathology/Powdery-Mildew)

### Media
- The images used on the Home and News Categories pages for logo and news posts were taken from [Google Images](https://images.google.nl/)

## Acknowledgements (optional)
- I acknowledge all the tutors fellow students at [Slack](https://app.slack.com/client/T0L30B202/D03PENWED0F) for their guidance to complete Image Identification.
- I acknowledge [Precious Ijege](https://www.linkedin.com/in/precious-ijege-908a00168/) for mentor support and finishing touches.