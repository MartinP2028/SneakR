<template>
  <div>
    <nav
      class="navbar flex justify-between items-center p-4 bg-white shadow-md grid grid-cols-1 md:grid-cols-3 gap-4"
    >
      <div class="nav_left flex justify-start items-center space-x-4">
        <p class="nav_item font-bold"><a href="/">HOME</a></p>
        <p class="nav_item font-bold"><a href="/collection">COLLECTION</a></p>
        <p class="nav_item font-bold"><a href="/wishlist">WISHLIST</a></p>
      </div>
      <div class="div_header flex justify-center items-center">
        <a href="/">
          <img class="logo w-20" src="../img/logo.png" alt="logo" />
        </a>
      </div>
      <div class="nav_right flex justify-end items-center">
        <UDropdown :items="items" mode="click">
          <p class="login font-bold">ACCOUNT</p>
          <template #item="{ item }">
            <span :class="{
              'truncate text-red-500': item.label === 'LogOut',
              'truncate text-black': item.label !== 'LogOut',
            }"
            >
              {{ item.label }}
            </span>
          </template>
        </UDropdown>
      </div>
    </nav>
  </div>
</template>

<script setup lang="js">
const user = useSupabaseUser();
const supabase = useSupabaseClient();

function logOut() {
  supabase.auth.signOut();
  reloadNuxtApp();
}

const items = user.value
  ? [
      [
        {
          label: "Log as " + user.value.email,
        },
      ],
      [
        {
          label: "LogOut",
          click: async () => {
          try {
            const { error } = await supabase.auth.signOut();
            if (error) {
              throw error;
            } else {
              console.log("logOut");
              reloadNuxtApp();
            }
          } catch (error) {
            console.log(error);
          }
        },
        },
      ],
    ]
  : [
      [
        {
          label: "Login",
          to: "/login",
        },
      ],
      [
        {
          label: "Register",
          to: "/register",
        },
      ],
    ];
</script>
