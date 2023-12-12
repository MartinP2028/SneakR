<template>
  <article class="grid">
    <div class="element bg-gray-200 p-4 rounded-lg shadow-md flex flex-col">
      <div class="img w-full h-full rounded-lg">
        <a :href="'/details/' + props.Sneakers.id">
          <img
            v-if="Sneakers['image.small']"
            class="img w-full h-full rounded-lg"
            :src="Sneakers['image.small']"
            alt="image of sneaker"
          />
        </a>
      </div>
      <div class="product_infos flex flex-col">
        <a :href="'/details/' + props.Sneakers.id">
          <p class="name text-xl font-bold mt-2">
            {{ Sneakers.brand }} {{ Sneakers.silhouette }}
          </p>
          <p class="colorway text-gray-500">{{ Sneakers.colorway }}</p>
        </a>
        <p class="price text-gray-500 font-bold mt-2">
          ${{ Sneakers.estimatedMarketValue }}
        </p>
      </div>
      <div class="add_to_buttons flex flex-col">
        <button
          v-if="!isInCollection"
          @click="addToCollection"
          class="bg-black text-white mt-2 py-2 px-4 rounded-lg hover:bg-gray-800"
        >
          ADD TO COLLECTION
        </button>
        <button
          v-else
          @click="removeFromCollection"
          class="bg-white text-black mt-2 py-2 px-4 rounded-lg hover:bg-gray-200">
          REMOVE FROM COLLECTION
        </button>
        <button
          v-if="!isInWishlist"
          @click="addToWishlist()"
          class="bg-black text-white mt-2 py-2 px-4 rounded-lg hover:bg-gray-800"
        >
          ADD TO WISHLIST
        </button>
        <button
          v-else
          @click="removeFromWishlist()"
          class="bg-white text-black mt-2 py-2 px-4 rounded-lg hover:bg-gray-200"
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
const isInCollection = ref(false);

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

function addToCollection() {
  console.log("add to collection");
  console.log(props.Sneakers);
  isInCollection.value = true;
}

function removeFromCollection() {
  console.log("remove from collection");
  console.log(props.Sneakers);
  isInCollection.value = false;
}
</script>
