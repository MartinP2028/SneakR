<template>
  <article class="grid">
    <div class="element bg-gray-200 p-4 rounded-lg shadow-md flex flex-col">
      <div class="img w-full h-full rounded-lg">
        <nuxt-link :to="'/details/' + props.Sneakers.id">
          <img
            v-if="Sneakers['image.small']"
            class="img w-full h-full rounded-lg"
            :src="Sneakers['image.small']"
            alt="image of sneaker"
          />
        </nuxt-link>
      </div>
      <div class="product_infos flex flex-col">
        <nuxt-link :to="'/details/' + props.Sneakers.id">
          <p class="name text-xl font-bold mt-2">{{ Sneakers.name }}</p>
          <p class="colorway text-gray-500">{{ Sneakers.colorway }}</p>
        </nuxt-link>
        <p class="price text-gray-500 font-bold mt-2">
          ${{ Sneakers.estimatedMarketValue }}
        </p>
      </div>
      <div class="add_to_buttons flex flex-col">
        <button class="bg-black text-white mt-2 py-2 px-4 rounded-lg">
          ADD TO COLLECTION
        </button>
        <button
          v-if="!isInWishlist"
          @click="addToWishlist()"
          class="bg-black text-white mt-2 py-2 px-4 rounded-lg"
        >
          ADD TO WISHLIST
        </button>
        <button
          v-else
          @click="removeFromWishlist()"
          class="bg-white text-red-500 mt-2 py-2 px-4 rounded-lg"
        >
          REMOVE FROM WISHLIST
        </button>
      </div>
    </div>
  </article>
</template>

<script setup>
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
