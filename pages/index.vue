<template>
  <section>
    <div>
      <Navbar />
      <Searchbar />
      <div
        class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-4 bg-gray-100"
      >
        <ListSneakers
          class="border rounded-lg border-shadow-2"
          v-for="Sneakers in Sneaker"
          :Sneakers="Sneakers"
        />
      </div>
      <Pagination />
    </div>
  </section>
</template>

<script setup>
const client = useSupabaseClient();

const { data: Sneaker } = await useAsyncData("Sneaker", async () => {
  const { data } = await client
    .from("Sneaker")
    .select("*")
    .order("brand")
    .range(0, 23);
  return data;
});
</script>
