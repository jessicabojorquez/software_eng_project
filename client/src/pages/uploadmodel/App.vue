<template>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="stylesheet" 
          href=
"https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
</head>
<body>


<!-- Navbar-->
<header class="header">
    <nav class="navbar">
        <div class="top-container"><a href="#" class="navbar-logo text-uppercase font-weight-bold">See-NN</a>
            <div id="navbarSupportedContent" class="collapse navbar-collapse">
                <ul class="navbar-nav">
                    <li class="nav-item"><a href="index.html" class="nav-menu-options text-uppercase font-weight-bold">Home</a></li> 
                </ul>
            </div>
        </div>
    </nav>
</header>

<div class="input-area">

    <!--Buttons to upload 3 files-->
    <form enctype="multipart/form-data" method="post" name="fileinfo"  id="form">

       
            
            <!--Button to upload .pth-->
            <div class="custom-file-upload in-all">



                <label class="custom-file-upload upload1"> 
                    <i class="fa fa-cloud-upload"></i>  Upload PyTorch file with extension <strong>.pth</strong>:
                    <input  type="file" name="pytorch_file" required />
                </label>

                <label class="custom-file-upload upload2">
                    <i class="fa fa-cloud-upload" aria-hidden="true"></i>  Upload Python file with extension <strong>.py</strong>:
                    <input type="file" name="python_file" required />
                </label>

                <label class="custom-file-upload upload3">
                    <i class="fa fa-cloud-upload" aria-hidden="true"></i>    Upload Image <strong>jpeg</strong> or <strong>png</strong>: <br>
                    <input type="file" name="input_image" required />
                </label>

                <input type="submit" value="Submit!" />

                <!--
                <input id="fileUpload" type="file" hidden>
                Upload PyTorch File: <br>
                <button @click="chooseFiles()">Upload <strong>.pth</strong></button>
                <br>
                <br>
                <br>
                <input id="fileUpload" type="file" hidden>
                Upload Python File:  <br>
                <button @click="chooseFiles()">Upload <strong>.py</strong></button>
                <br>
                <br>
                <br>
                <input id="fileUpload" type="file" hidden>
                Upload Image:  <br>
                <button @click="chooseFiles()">Upload <strong>.jpeg</strong>/<strong>.png</strong></button>
                -->


            </div>
        </form>
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
        height: 150%; /*600px;*/
        font-family: Arial;
        color: chocolate;
        /*border: none;*/
        /*border-color: red;*/
        border-radius:10px  /*round corner*/
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
        background-color:cornflowerblue;
        transition: 0.5s;
        box-shadow: 0 0 0 4px DarkOliveGreen;
    }

    .left-button:hover {
        background-color:cornflowerblue;
        transition: 0.5s;
        box-shadow: 0 0 0 4px DarkOliveGreen;
    }

    .right-button:focus {
        outline-color: transparent;
        outline-style:solid;
        box-shadow: 0 0 0 4px olive;
    }

    .left-button:focus {
        outline-color: transparent;
        outline-style:solid;
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
        font-family: Impact,Cursive, sans-serif;
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

    .team{
        width:500px; /* or whatever width you want. */
        max-width:500px; /* or whatever width you want. */
    }

    /*Upload Model styling*/
    input[type="file"] {
        color: DarkKhaki;
    }

   
    .input-area {
        color: olive;
        height: 500px; 
        position: relative;
    }

    .custom-file-upload {
        display: inline-block;
        padding: 6px 12px;
        cursor: pointer;
        background-color: beige;
        height: 240px;
        width: 600px;
        color: olive;
        position: absolute;
        
    }
    .upload1 {
        position: relative;
        height: 50px;
    }

    .upload2 {
        position: relative;
        height: 50px;
    }

    .upload3 {
        position: relative;
        height: 50px;
    }
    
</style>
