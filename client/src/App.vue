<!--Some notes:
h1 has the tittle, don't use h1 on anything else so that the css does not get confusing
-->


<template>
  <div class="home-page">
    <!--The top bar holding the website tittle and the "buttons-div" -->
    <div class="top-bar">

      <div class="website-tittle">
        <h1>See-NN</h1>
      </div>

      <!--menu class holds the buttons-->
      <div class="buttons-div">

        
        <!--Upload Model-->
        <div class="upload-model-div">
          <UploadButtonVue />
        </div>

        <!--Upload Images
        <div class="upload-images-div">
          <button @click="toggleSomeFlag_2">
            <span v-if="images_uploaded">Upload Images</span>
            <span v-else>Insert Drop Down Menu</span>
          </button>
          
        </div>-->
        
        <!--Available Models-->
        <div class="available-models-div">
          <FlagButtonVue v-bind='available_models'/>
        </div>

        <!--Upload
        <a href="#" class="upload-button-div">
          <button @click="toggleSomeFlag_4">
            <span v-if="upload_pushed">Upload</span>
            <span v-else>Refresh</span>
          </button>
        </a>-->

        <!--Round Button-->
        <a href="#" class="round-button" @click="toggleSomeFlag_1">
          <div class="play-arrow-right"></div>
          <!-- To help see how this button works, uncomment this and comment next  2 lines of code
            (left like this to add functionality later)
          <span v-if="someFlag">Play</span>
          <span v-else>Upload</span>
          -->
          <span v-if="someFlag"></span>
          <span v-else>Upload</span>
        </a>

      </div>
    </div>
  </div>
</template>

<script>
//import { MDBBtn, MDBIcon } from "mdb-vue-ui-kit";
import UploadButtonVue from './components/UploadButton.vue'
import FlagButtonVue from './components/FlagButton.vue'
import uploadFile from './API/API'
export default {
  name: 'App',
  components: {
    UploadButtonVue,
    FlagButtonVue
    //MDBBtn,
    //MDBIcon
  },

  data () {
    return {
      //variables to set to true or false or to use for function calling
      available_models:{
            msgClicked:'Drop-Down List',
            msgNotClicked:'Select Available Model'
        },
      model_uploaded: true,
      images_uploaded: true,
      display_available_models: true,
      upload_pushed: true
    }
  },
  methods: {
    //toy functions to then be replaced by real functions that do stuff for cnn visualizations
    toggleSomeFlag_1() {
      console.log("hello")
      uploadFile()
    },
    toggleSomeFlag_2() {
            this.images_uploaded = !this.images_uploaded
    },
    toggleSomeFlag_3() {
            this.display_available_models = !this.display_available_models
    },
    toggleSomeFlag_4() {
            this.upload_pushed = !this.upload_pushed
    }
  }
}

</script>

<!--The "scoped" attribute limits CSS to this component only, if removed the font is orchid-->
<style scoped>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  /*text-align: center;*/
  /* color: #2c3e50; */
  /*margin-top: 60px;*/
  color:orchid
}

/**background of whole website */
body {
  background:whitesmoke
}

/**background of top box holding title and buttons */
.top-bar{
  background:rgb(81, 66, 128)
}

/**div hat holds the 5 current buttons 10/31/22 (may change in future) */
.buttons-div {
  display:flex;
  align-items: center;
  justify-content: space-around;
}

/**buton 1 */
.upload-model-div {
  flex:1;
  border: 0px;
  text-align: center;
}

/**buton 2 */
.upload-image-div {
  flex:1;
  border: 0px;
  text-align: center;
}

/**buton 3 */
.available-models-div {
  flex:1;
  border: 0px;
  text-align: center;
}

/**buton 4 */
.upload-button-div {
  background-color: #04AA6D; /* Green */
  border: none;
  color: white;
  padding: 20px;
  text-align: center;
  text-decoration: none;
  display: inline-block;
  font-size: 26px;
  margin: 4px 4px;
  cursor: pointer;
  background: transparent;
  
}

/**buton 5 (round button) */
.round-button {
	box-sizing: border-box;
	display:block;
	width:80px;
	height:80px;
	padding-top: 14px;
	padding-left: 8px;
	line-height: 20px;
	border: 0px solid rgba(0,0,0,0.5);
	border-radius: 50%;
	color:#f5f5f5;
	text-align:center;
	text-decoration:none;
	background-color: rgba(0,0,0,0.5);
	font-size:20px;
	font-weight:bold;
	transition: all 0.3s ease;
}

/**buton 5(also round button) */
.round-button:hover {
	background-color: rgba(0,0,0,0.8);
	box-shadow: 0px 0px 10px rgba(255,255,100,1);
	text-shadow: 0px 0px 10px rgba(255,255,100,1);
}

/**buton 5 (the triangle inside it, needs to be centers) */
.play-arrow-right {
  position:absolute;
  right: 28px;
  top:95px;
  width: 0; 
  height: 0; 
  border-top: 20px solid transparent;
  border-bottom: 20px solid transparent;
  border-left: 30px solid green;
  float:initial;
}

/**_______________________________________h1 start (modify inside)______________________________ */
/**h1 is the tittle See-NN */
h1 {
  position: relative;
  padding: 0;
  margin: 0;
  font-family: "Raleway", sans-serif;
  font-weight: 300;
  font-size: 40px;
  color: #080808;
  -webkit-transition: all 0.4s ease 0s;
  -o-transition: all 0.4s ease 0s;
  transition: all 0.4s ease 0s;
}
/**h1 is the tittle See-NN */
h1 span {
  display: block;
  font-size: 0.5em;
  line-height: 1.3;
}
/**h1 is the tittle See-NN */
h1 em {
  font-style: normal;
  font-weight: 600;
}
/**h1 is the tittle See-NN */
.website-tittle h1 {
  font-size:26px; font-weight:700;  letter-spacing:1px; text-transform:uppercase; width:160px; text-align:center; margin:auto; white-space:nowrap; padding-bottom:13px;
}
/**h1 is the tittle See-NN */
.website-tittle h1:before {
    background-color: green;
    content: '';
    display: block;
    height: 3px;
    width: 75px;
    margin-bottom: 5px;
}
/**h1 is the tittle See-NN */
.website-tittle h1:after {
    background-color: green;
    content: '';
    display: block;
  position:absolute; right:0; bottom:0;
    height: 3px;
    width: 75px;
    margin-bottom: 0.25em;
}
/**_______________________________________h1 end_______________________________________________ */

</style>
