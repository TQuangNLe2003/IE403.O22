# IE403_DataMining
Course Project - "Detection of Spam Comments on the Shopee Social Media Platform in Vietnam"

Instructions to Run app.py:
- Download the app.py file: Obtain the app.py file from the provided resource or copy the supplied source code.

- Install the required libraries: Open a terminal and run the following commands to install the necessary libraries:
                  pip install streamlit torch transformers Pillow
  
- Adjust the appropriate file paths: In the app.py source code, ensure that the paths to the bert_model.pth file, the tokenizer directory, and the image folder are correctly specified.
- Run the app: Open the terminal and run the following command:
                  streamlit run app.py
- Access the web app: After running the command, a web browser will automatically open, displaying the demo web application. Enter a text into the input field and click the "Predict" button to see the model's prediction on whether the input text is spam or not.
