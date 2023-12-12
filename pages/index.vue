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
      <div class="flex justify-center mt-4">
        <UPagination size="md" v-model="current_pagination" :page-count="28" :max="8" :total="49214" show-last show-first />
      </div>
    </div>
  </section>
</template>

<script setup>
const supabase = useSupabaseClient();
const current_pagination = ref(1);
const sneakersPerPage = 28;

const { data: Sneaker } = await useAsyncData("Sneaker", async () => {
  const { data } = await supabase
    .from("Sneaker")
    .select("*")
    .range(current_pagination.value * sneakersPerPage - sneakersPerPage, current_pagination.value * sneakersPerPage - 1);
  return data;
});

watch(current_pagination, async () => {
  const { data: Sneaker } = await useAsyncData("Sneaker", async () => {
    const { data } = await supabase
      .from("Sneaker")
      .select("*")
      .range(current_pagination.value * sneakersPerPage - sneakersPerPage, current_pagination.value * sneakersPerPage - 1);
    window.scrollTo(0, 0);
    return data;
  });
});

</script>
