<template>
  <article class="grid">
    <div class="element bg-gray-200 p-4 rounded-lg shadow-md flex flex-col">
      <div class="img w-full h-full rounded-lg">
        <img
          v-if="Sneakers['image.small']"
          class="img w-full h-full rounded-lg"
          :src="Sneakers['image.small']"
          alt="image of sneaker"
        />
      </div>
      <div class="product_infos flex flex-col">
        <p class="name text-xl font-bold mt-2">{{ Sneakers.name }}</p>
        <p class="colorway text-gray-500">{{ Sneakers.colorway }}</p>
        <p class="price text-gray-500 font-bold mt-2">
          ${{ Sneakers.estimatedMarketValue }}
        </p>
      </div>
      <div class="add_to_buttons flex flex-col">
        <button class="bg-black text-white mt-2 py-2 px-4 rounded-lg">
          ADD TO COLLECTION
        </button>
        <button
          @click="addToWishlist()"
          class="bg-black text-white mt-4 py-2 px-4 rounded-lg"
        >
          ADD TO WISHLIST
        </button>
      </div>
    </div>
  </article>
</template>

<script setup>
const props = defineProps(["Sneakers"]);
function addToWishlist() {
  console.log("add to wishlist");
  console.log(props.Sneakers);
}
</script>
