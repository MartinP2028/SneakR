<template>
  <section>
    <div>
      <Navbar />
      <Searchbar />
      <ListSneakers v-for="Sneakers in Sneaker" :Sneakers="Sneakers" />
      <Pagination />
    </div>
  </section>
</template>

<script setup>
const client = useSupabaseClient();

const { data: Sneaker } = await useAsyncData("Sneaker", async () => {
  const { data } = await client.from("Sneaker").select("['image.small'], name, estimatedMarketValue").order("brand").range(0, 10);
  return data;
});

// console.log(Sneaker.value);
</script>
