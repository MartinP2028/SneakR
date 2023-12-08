<template>
  <article>
    <img class="img" :src="Sneakers['image.small']" alt="image of sneaker" />
    <p class="name">{{ Sneakers.name }}</p>
    <p class="price">${{ Sneakers.estimatedMarketValue }}</p>
    <button class="bg-gray-200 mr-2">ADD TO WISHLIST</button>
    <button class="bg-gray-200">ADD TO COLLECTION</button>
  </article>
</template>

<script setup>
const props = defineProps(["Sneakers"]);
</script>
