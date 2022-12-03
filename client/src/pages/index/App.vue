<script>
/**
 * Index Page
 * @vue-event {Null} upload_func  - Changes page to /uploadmodel.html
 * @vue-event {Null} use_func  - Changes page to /library.html
 */
export default {
    methods: {

        upload_func() {
            window.location.href = "uploadmodel.html";
        },
        use_func() {
            window.location.href = "library.html";
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
                <div class="top-container"><a href="#" class="navbar-logo text-uppercase font-weight-bold">See-NN</a>

                    <div id="navbarSupportedContent" class="collapse navbar-collapse">
                        <ul class="navbar-nav">
                            <li class="nav-item"><a href="#"
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

        <div class="bottom-container" id="bottom-container">


            <button @click="upload_func()" type="button" class="split left-button" id="upload-button">
                <img src="../../assets/icons8-upload-50.png" alt="Avatar woman">
                <h2>Upload Model</h2>
                <p>Upload your own model.</p>

            </button>



            <button @click="use_func()" type="button" class="split right-button" id="use-existing-button">
                <div class="centered">
                    <img src="../../assets/icons8-magnifying-glass-tilted-left-48.png" alt="Avatar man">
                    <h2>Use Existing Model</h2>
                    <p>Use one of ours.</p>
                </div>
            </button>

        </div>
    </body>
</template> 

<style>
body {
    font-family: Arial;
    color: black;
    background-color: beige;
}

.bottom-container {
    position: relative;
    background-color: ivory;
    height: 600px;
}

.split {
    position: absolute;
    width: 50%;
    height: 100%;
    font-family: Arial;
    color: white;
    border-radius: 10px



}

.left-button {
    left: 0%;
    background-color: DarkKhaki;

}

.right-button {
    right: 0%;
    background-color: DarkKhaki;
}

.right-button:hover {
    background-color: BurlyWood;
    /*olive;*/
    transition: 0.5s;
    box-shadow: 0 0 0 4px DarkOliveGreen;
}

.left-button:hover {
    background-color: BurlyWood;
    /*olive;*/
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
    font-size: 5.6em;
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