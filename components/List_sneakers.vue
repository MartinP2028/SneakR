<template>
    <article class="grid">
        <div class="element bg-gray-200 p-4 rounded-lg shadow-md">
            <div class="img w-full h-64 rounded-lg">
                <img v-if="Sneakers['image.small']" class="w-full h-full object-cover rounded-lg" :src="Sneakers['image.small']" alt="image of sneaker" />
            </div>
            <p class="name text-xl font-bold mt-2">{{ Sneakers.name }}</p>
            <p class="colorway text-gray-500">{{ Sneakers.colorway }}</p>
            <p class="price text-gray-500 font-bold mt-2">${{ Sneakers.estimatedMarketValue }}</p>
            <button class="bg-black text-white mt-4 py-2 px-4 rounded-lg">ADD TO WISHLIST</button>
            <button class="bg-black text-white mt-2 py-2 px-4 rounded-lg">ADD TO COLLECTION</button>
        </div>
    </article>
</template>

<script setup>
const props = defineProps(["Sneakers"]);
</script>
