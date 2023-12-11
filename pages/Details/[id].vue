<template>
  <section>
    <div>
      <Navbar />
      <Searchbar />
      <div class="grid">
        <Detailed_sneaker {{ route.params.id  }}
          class="border rounded-lg border-shadow-2"
          v-for="Sneakers in Sneaker"
          :Sneakers="Sneakers"
        />
      </div>
    </div>
  </section>
</template>

<script setup lang="ts">
const client = useSupabaseClient();
const route = useRoute();

const { data: Sneaker } = await useAsyncData("Sneaker", async () => {
  const { data } = await client
    .from("Sneaker")
    .select("['image.small'], name, estimatedMarketValue, colorway")
    .order("brand")
    .range(0, 11)
    .eq("id", route.params.id);
  return data;
});
</script>