<template>
  <article class="grid sm:grid-cols-1 lg:grid-cols-2">
    <div class="bg-gray-100 p-4 shadow-md">
      <div class="img w-full h-full rounded-lg">
        <img
          v-if="Sneakers['image.small']"
          class="w-full h-full rounded-lg"
          :src="Sneakers['image.small']"
          alt="image of sneaker"
        />
      </div>
    </div>
    <div class="bg-white p-4 shadow-md">
      <p class="text-xl font-bold mt-2">
        {{ Sneakers.name }}
      </p>
      <p class="text-gray-500">{{ Sneakers.colorway }}</p>
      <div class="mt-4">
        <p class="text-l font-bold">Brand:</p>
        <p>{{ Sneakers.brand }}</p>
      </div>
      <div class="mt-4">
        <p class="text-l font-bold">Silhouette:</p>
        <p>{{ Sneakers.silhouette }}</p>
      </div>
      <div class="mt-4">
        <p class="text-l font-bold">Retail Price:</p>
        <p>${{ Sneakers.retailPrice }}</p>
      </div>
      <div class="mt-4">
        <p class="text-l font-bold">Estimated Market Value:</p>
        <p>${{ Sneakers.estimatedMarketValue }}</p>
      </div>
      <div class="mt-4">
        <p class="text-l font-bold">Release Date:</p>
        <p>{{ Sneakers.releaseDate }}</p>
      </div>
      <div class="mt-4">
        <p class="text-l font-bold">Gender:</p>
        <p>{{ Sneakers.gender }}</p>
      </div>
      <div class="mt-4">
        <button class="bg-black text-white mr-2 py-1 px-2 rounded-lg">
          ADD TO COLLECTION
        </button>
        <button
          v-if="!isInWishlist"
          @click="addToWishlist()"
          class="bg-black text-white mt-2 py-1 px-2 rounded-lg"
        >
          ADD TO WISHLIST
        </button>
        <button
          v-else
          @click="removeFromWishlist()"
          class="bg-white text-black border border-black mt-2 py-1 px-2 rounded-lg"
        >
          REMOVE FROM WISHLIST
        </button>
      </div>
      <div class="mt-4">
        <p class="text-l font-bold">Story:</p>
        <p>{{ Sneakers.story }}</p>
      </div>
    </div>
  </article>
</template>

<script setup>
import { defineProps, ref } from 'vue';

const props = defineProps(["Sneakers"]);
const isInWishlist = ref(false);

function addToWishlist() {
  console.log("add to wishlist");
  console.log(props.Sneakers);
  isInWishlist.value = true;
}

function removeFromWishlist() {
  console.log("remove from wishlist");
  console.log(props.Sneakers);
  isInWishlist.value = false;
}
</script>
