<script>

export default {
  props:{
    src: String
  },
  data() {
    return {
        dataList: [],
        subdir: String
    };
  },
  created() {
    const queryString=window.location.search
    const urlParams = new URLSearchParams(queryString);
    const myURL=urlParams.get('name')
    this.subdir=myURL+'/'
    var path=this.subdir+"output.json";
    fetch(path)
            .then(response => response.json())
            .then(data => (this.dataList = data));
  },
  computed:{
    numLayers() {
        return this.dataList.info.num_layers
    },
    imagePaths() {
        var temp=[]
        for (let i = 0; i<this.numLayers;i++)
        {
            //temp[i]="../../../public/test/"+this.dataList.layer_info[i].output_path.substring(2);
            temp[i]=this.subdir+this.dataList.layer_info[i].output_path.substring(2);
        }
        return temp
    },
    imageLabels() {
        var temp=[]
        for (let i = 0; i<this.numLayers;i++)
        {
            var base=this.dataList.layer_info[i]

            temp[i]=base.output_shape[1]+' * '+base.output_shape[2]+' * '+base.output_shape[3]
        }
        return temp
    },
    isActive() {
        var temp = []
        for (let i = 0; i<10;i++)
        {
            if (i<this.numLayers)
            {
                temp[i]=true;
            }
            else {
                temp[i]=false;
            }
        }
        return temp
    },
    imageHeight() {
        let height=screen.height
        return height/4
    }
  },
  methods: {
  }
};
</script>




<template>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1">

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

<div class="team">

        <div class="grid-container" :class="{ four: numLayers==4, six: numLayers==6, eight:numLayers==8, ten: numLayers==10}" >
        <figure class="grid-item" :class="{ hide: !isActive[0]}">
        <img :src="imagePaths[0]" :height=imageHeight alt="">
        <figcaption>{{imageLabels[0]}}</figcaption>
        </figure>

        <figure class="grid-item" :class="{ hide: !isActive[1]}">
        <img :src="imagePaths[1]" :height=imageHeight alt="">
        <figcaption>{{imageLabels[1]}}</figcaption>
        </figure>

        <figure class="grid-item" :class="{ hide: !isActive[2]}">
        <img :src="imagePaths[2]" :height=imageHeight alt="">
        <figcaption>{{imageLabels[2]}}</figcaption>
        </figure>

        <figure class="grid-item" :class="{ hide: !isActive[3]}">
        <img :src="imagePaths[3]" :height=imageHeight alt="">
        <figcaption>{{imageLabels[3]}}</figcaption>
        </figure>

        <figure class="grid-item" :class="{ hide: !isActive[4]}">
        <img :src="imagePaths[4]" :height=imageHeight alt="">
        <figcaption>{{imageLabels[4]}}</figcaption>
        </figure>

        <figure class="grid-item" :class="{ hide: !isActive[5]}">
        <img :src="imagePaths[5]" :height=imageHeight alt="">
        <figcaption>{{imageLabels[5]}}</figcaption>
        </figure>

        <figure class="grid-item" :class="{ hide: !isActive[6]}">
        <img :src="imagePaths[6]" :height=imageHeight alt="">
        <figcaption>{{imageLabels[6]}}</figcaption>
        </figure>

        <figure class="grid-item" :class="{ hide: !isActive[7]}">
        <img :src="imagePaths[7]" :height=imageHeight alt="">
        <figcaption>{{imageLabels[7]}}</figcaption>
        </figure>

        <figure class="grid-item" :class="{ hide: !isActive[8]}">
        <img :src="imagePaths[8]" :height=imageHeight alt="">
        <figcaption>{{imageLabels[8]}}</figcaption>
        </figure>

        <figure class="grid-item" :class="{ hide: !isActive[9]}">
        <img :src="imagePaths[9]" :height=imageHeight alt="">
        <figcaption>{{imageLabels[9]}}</figcaption>
        </figure>

        </div>
    </div>


<div class="bottom-container" id ="bottom-container">
    
    
   


</div>
</body>
</template> 

<style>
    .grid-container {
      display: grid;
      padding: 10px;
      align-self: center;
    }

    .four {
    grid-template-columns: auto auto;
    }

    .six {
    grid-template-columns: auto auto auto;
    }

    .eight {
    grid-template-columns: auto auto auto auto;
    }

    .ten {
    grid-template-columns: auto auto auto auto;
    }
    .grid-item {
      background-color: rgba(255, 255, 255, 0.8);
      border: 1px solid rgba(0, 0, 0, 0.8);
      padding: 20px;
      font-size: 40px;
      text-align: center;
      font-weight:bold;
    }
    .hide {
      display:none;
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
        font-size: 5.6em;
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

</style>