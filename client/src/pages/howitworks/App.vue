
<template>

    <head>
        <meta name="viewport" content="width=device-width, initial-scale=1">

    </head>

    <body>


        <!-- Navbar-->
        <header class="header">
            <nav class="navbar">
                <div class="top-container"><a href="index.html"
                        class="navbar-logo text-uppercase font-weight-bold">See-NN</a>
                    <div id="navbarSupportedContent" class="collapse navbar-collapse">
                        <ul class="navbar-nav">
                            <li class="nav-item"><a href="index.html"
                                    class="nav-menu-options text-uppercase font-weight-bold">Home</a></li>
                        </ul>
                    </div>
                </div>
            </nav>
        </header>

        <div class="team">

            <p>
                When you upload your own model and image or select one of our pretrained ones, we first tell our server what models/images to use. This is then passed to our visualizer code, which uses an algorithm called Grad-CAM. This algorithm takes as input a neural network, an image, and a class we are interested in (generally the class of the image we passed in). It then take the class of interest, and backpropogates only the gradients that relate to this class. In this way, we can see which parts of the image are most influential on picking this class and can see whether these are the areas we want the network to focus on or not. 

                For our particular application, we ask the algorithm to focus specifically on a few convolutional layers rather than the entire network (which would include pooling layers and fully connected layers as well). This allows us to get useful results without presenting the user with an overload of information, much of which might not be very useful. 

                After running the algorithm, we package the results in a json file which is passed back from our backend the frontend and then visualized with Vue.js.
        </div>

        <div class="bottom-container" id="bottom-container">





        </div>
    </body>
</template> 

<style>
body {
    font-family: Arial;
    color: black;
    background-color: beige;
}

/*
    .top {
        background-color: ivory; 
    }*/

.bottom-container {
    position: relative;
    background-color: ivory;
    height: 600px;
}

.split {
    position: absolute;
    width: 50%;
    height: 150%;
    /*600px;*/
    font-family: Arial;
    color: chocolate;
    /*border: none;*/
    /*border-color: red;*/
    border-radius: 10px
        /*round corner*/
        /*box-shadow: 0px 0px 2px 2px rgb(0,0,0)*/
        /*padding:15px;
        min-height:30px; 
        min-width: 120px;*/


}

.left-button {
    left: 0%;
    background-color: cornsilk;

}

.right-button {
    right: 0%;
    background-color: cornsilk;
}

.right-button:hover {
    background-color: cornflowerblue;
    transition: 0.5s;
    box-shadow: 0 0 0 4px DarkOliveGreen;
}

.left-button:hover {
    background-color: cornflowerblue;
    transition: 0.5s;
    box-shadow: 0 0 0 4px DarkOliveGreen;
}

.right-button:focus {
    outline-color: transparent;
    outline-style: solid;
    box-shadow: 0 0 0 4px olive;
}

.left-button:focus {
    outline-color: transparent;
    outline-style: solid;
    box-shadow: 0 0 0 4px olive;
}

.right-button:active {
    background-color: #ffbf00;
}

.left-button:active {
    background-color: #ffbf00;
}





/*Navigation Bar*/
.navbar {
    transition: all 0.4s;
    background-color: ivory;
}

.navbar .nav-menu-options {
    color: DarkOliveGreen;
}

.navbar .nav-menu-options:hover,
.navbar .nav-menu-options:focus {
    color: DarkOliveGreen;
    text-decoration: none;
}

.navbar .navbar-logo {
    color: DarkOliveGreen;
    font-size: 3.6em;
    font-family: Impact, Cursive, sans-serif;
    /*border: 3px solid green;
        padding: 10px;*/
    text-align: center;
}




/*See-NN*/
.font-weight-bold {
    font-weight: bold;
}

.text-uppercase {
    text-transform: uppercase;
}

ul {
    list-style-type: none;
    margin: 0;
    padding: 0;
}


/*Bar*/
li {
    float: left;
}

a {
    display: block;
    padding: 8px;
    background-color: #dddddd;
}

ul {
    background-color: #dddddd;
}

ul {
    list-style-type: none;
    margin: 0;
    padding: 0;
    overflow: hidden;
    background-color: #333;
}

li {
    float: left;
}

li a {
    display: block;
    color: white;
    text-align: center;
    padding: 14px 16px;
    text-decoration: none;
    background-color: #333;
}

/* Change the link color to #111 (black) on hover */
li a:hover {
    background-color: #111;
}

.active {
    background-color: #04AA6D;
}

.team {
    width: 500px;
    /* or whatever width you want. */
    max-width: 500px;
    /* or whatever width you want. */
}
</style>