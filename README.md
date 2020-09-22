# Neural-Network-Visualizer-Web-App-with-Python

### Video1: Introduction
We will visualize the output of all the nodes of all the layer produced by a simple neural network with 2 hidden layers and a output layer.

### Video2: The Dataset
Refer the ipynb file for loading data, viewing data with matplotlib.

### Video3: Data Normalization
- Change the 28*28 array to 1*784 array (Link joining images side by side)
- Normalize the values from 0 to 1 so that model training gets easy.

### Video4: Create and train a model
- Setup model layers, nodes , activation function
- Compile model with loss, optimizer
- Train model with model.fit()
- Save the trained model with model.h5

### Video5: Create a model server with Flask
- %%writefile - line magic function in jupyter to create and write file from notebook itself.
- Created a basic flask server and got it running

### Video6: Create a model server with Flask Continued
- The model we saved will give the final predictions only and not the values of intermediate hidden layers.
- So create another model which takes the same input as the previous model and gives list of output of all layers.
- Allowing POST requests in Flask and send a random image with its prediction over the POST request.
- Next lets start working on the client side to use the predictions and visualize them.

### Video7: Streamlit Web application
- Can develop frontend for our apps without much web development knowledge.
- Now our application frontend makes call to the ml_server and gets the predictions & image and shows it in the frontend.

### Video8: Streamlit Web application continued
- Showing image in sidebar with streamlit.sidebar()
- Getting reponse from ml_server with POST request using requests library
- Adding some functions and completing the working app
