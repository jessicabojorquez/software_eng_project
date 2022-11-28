<script>

export default {
    data() {
        return {
            source: "../../assets/output.json"
        }
    },
    methods: {
        output_func() {
            window.location.href = "output.html?name=test";
        },
        output_func2() {
            window.location.href = "output.html?name=test2";
        },
        output_func3() {
            window.location.href = "output.html?name=test3";
        },
        output_func4() {
            window.location.href = "output.html?name=test4";
        },
    }
}
</script>

<template>

    <head>
        <meta name="viewport" content="width=device-width, initial-scale=1">

    </head>

    <body>

        <!-- ADDED <a> TAG TO TRY TO DO THE GOVER THING ON THE BUTTON WITH DIFF color
    MIGHT NEED OT WATCH TUTORIAL TO SEE HOW TO CHANGE THAT   
    i DO HAVE A BUTTON ABOVE FOR TESTING
    THE COLOR GREEN ONT HE BUTOTN IS GIVING ISSUES

    ********
    TRY TO REMOVE THE COLOR GREEN AND SEE IF ITS HOVERS 
-->

        <!--
<div class="top" id="top">
    <div class="centered">
        <h2>Page Tittle</h2>
        <p>Some text.</p>
    </div>
    <button class="hi">hi

        <img src="img_avatar.png" alt="Avatar man">
    </button>
</div>-->
        <!-- Navbar-->
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


            <button @click="output_func()" :src=source type="button" class="grid-item " id="upload-button">
                <!--<div class="centered">-->
                <img src="../../assets/icons8-mind-map-50.png" alt="Avatar woman" width="100">
                <h2>Choose Model 1</h2>
                <p>This model blah blah.</p>

                <!--</div>-->
            </button>

            <button @click="output_func2()" type="button" class="grid-item" id="use-existing-button">
                <div class="centered">
                    <img src="../../assets/icons8-mind-map-50.png" alt="Avatar man" width="100">
                    <h2>Choose Model 2</h2>
                    <p>This model blah blah.</p>
                </div>
            </button>

            <button @click="output_func3()" type="button" class="grid-item" id="use-existing-button" height="100">
                <div class="centered">
                    <img src="../../assets/icons8-mind-map-50.png" alt="Avatar man" width="100">
                    <h2>Choose Model 3</h2>
                    <p>This model blah blah.</p>
                </div>
            </button>

            <button @click="output_func4()" type="button" class="grid-item" id="use-existing-button">
                <div class="centered">
                    <img src="../../assets/icons8-mind-map-50.png" alt="Avatar man" width="100">
                    <h2>Choose Model 4</h2>
                    <p>This model blah blah.</p>
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