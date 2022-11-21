<!--

  UseOurs: The large "Use One of Ours" button on front page
  
  The Drawable component takes a height, width, and label, and creates a button of the specified size with the specified label, 
  whose background image should be in the assets field, and is linked to in the style component at the bottom. 
  The style component can also be customized with any other components that should be included.

  For dummy purposes, the button can also take a src, which should be an image link in triple quotes "'https://...'"
  If this is passed, the button will simply copy out this image whenever it is clicked.

  I am not currently pushing non-trivial functionality because it is incomplete and frequently breaks things.
-->

<script>

export default {
    name:'Drawable-button',
  props:{
    height: Number,
    width: Number,
    src: String,
    label: String
  },
  data(){
    return{
    }
  },
  computed:{
    styleObject() {
        return {
        height: this.height+'px',
        width: this.width+'px',
        //backgroundImage: 'url('+this.src+')',
        backgroundSize:'contain'
        }
      }
  },
  methods: {
    show_image(src, width, height) {
    var img = document.createElement("img");
    img.src = src.substring(1,src.length-1);
    img.width = width;
    img.height = height;
    document.body.appendChild(img);
    }
  }
}
</script>


<template>
    <button  :style=styleObject class=localBackground @click="show_image(src,width,height)"> {{label}} </button> 
</template>


<style>
.localBackground {
  background-image:url(../assets/logo.png);
}
</style>