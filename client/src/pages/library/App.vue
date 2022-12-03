<script>
/**
 * Library Page
 * @vue-data {String} source - static link to assets folder
 * @vue-event {String} output_func - changes page to output, and sets the URL parameter name to equal param
 */
export default {
    data() {
        return {
            source: "../../assets/output.json"
        }
    },
    methods: {
        output_func(param) {
            window.location.href = "output.html?name="+param;
        }
    }
}
</script>

<template>

    <head>
        <meta name="viewport" content="width=device-width, initial-scale=1">

    </head>

    <body>
        <header class="header">
            <nav class="navbar">
                <div class="top-container"><a href="index.html"
                        class="navbar-logo text-uppercase font-weight-bold">See-NN</a>

                    <div id="navbarSupportedContent" class="collapse navbar-collapse">
                        <ul class="navbar-nav">
                            <li class="nav-item"><a href="index.html"
                                    class="nav-menu-options text-uppercase font-weight-bold">Home</a></li>
                            <li class="nav-item"><a href="about.html"
                                    class="nav-menu-options text-uppercase font-weight-bold">About the Team</a></li>
                            <li class="nav-item"><a href="howitworks.html"
                                    class="nav-menu-options text-uppercase font-weight-bold">How it works</a></li>
                        </ul>
                    </div>
                </div>
            </nav>
        </header>

        <div class="grid-container" id="bottom-container">


            <button @click="output_func('seven')" :src=source type="button" class="grid-item " id="upload-button">
                <img src="../../assets/seven.jpg" alt="Avatar woman" width="100">
                <h2>3-layer CNN on MNIST dataset </h2>
                <p>This model contains 2 Conv layers, 2 pooling layers and 2 fully connected layers.</p>
                  <p>The input for this model is a grayscale image of digit 7. Our model predicts it correctly. </p>

            </button>

            <button @click="output_func('nine')" type="button" class="grid-item" id="use-existing-button">
                <div class="centered">
                    <img src="../../assets/nine.jpg" alt="Avatar man" width="100">
                    <h2> 3-layer CNN on MNIST dataset</h2>
                    <p> This model contains 2 Conv layers, 2 pooling layers and 2 fully connected layers.</p>
                  <p>The input for this model is a grayscale image of digit 9. Our model predicts it incorrectly.</p>
                </div>
            </button>

            <button @click="output_func('plane')" type="button" class="grid-item" id="use-existing-button" height="100">
                <div class="centered">
                    <img src="../../assets/plane.jpg" alt="Avatar man" width="100">
                    <h2>4-layer CNN on CFAIR-10 dataset</h2>
                    <p>This model contains 2 Conv layers, 2 pooling layers and 3 fully connected layers.</p>
                  <p>The input is a rgb image of a plane. Our model predicts it correctly.</p>
                </div>
            </button>

            <button @click="output_func('deer')" type="button" class="grid-item" id="use-existing-button">
                <div class="centered">
                    <img src="../../assets/deer.jpg" alt="Avatar man" width="100">
                    <h2>2-layer CNN on CFAIR-10 dataset</h2>
                    <p>This model contains 2 Conv layer, 2 pooling layer and 3 fully connected layers.</p>
                  <p>The input is a rgb image of a deer. Our model predicts it incorrectly.</p>
                </div>
            </button>

        </div>
    </body>
</template> 

<style>
.grid-container {
    display: grid;
    padding: 10px;
    align-self: center;
    grid-template-columns: auto auto
}

.grid-item {
    background-color: cornsilk;
    border: 1px solid rgba(0, 0, 0, 0.8);
    padding: 20px;
    font-size: 20px;
    text-align: center;
    font-weight: bold;
    font-family: Arial;
    color: DarkOliveGreen;
    border-radius: 10px
}

.grid-item:hover {
    background-color: BlanchedAlmond;
    /**Color of button when mouse goes on top */
    transition: 0.5s;
    box-shadow: 0 0 0 4px DarkOliveGreen;
}

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
    height: 50%;
    /*600px;*/
    font-family: Arial;
    color: DarkOliveGreen;
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
    /*DarkOliveGreen; */
}

.right-button:hover {
    background-color: BlanchedAlmond;
    /**Color of button when mouse goes on top */
    transition: 0.5s;
    box-shadow: 0 0 0 4px DarkOliveGreen;
}

.left-button:hover {
    background-color: BlanchedAlmond;
    transition: 0.5s;
    box-shadow: 0 0 0 4px DarkOliveGreen;
    /*DarkKhaki;*/
    ;
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
</style>