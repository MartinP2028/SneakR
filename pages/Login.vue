<template>
  <div>
    <Navbar />
    <section class="flex items-center justify-center py-100 sm:px-6 lg:px-8">
      <div class="max-w-md w-full space-y-8">
        <div>
          <h2 class="mt-6 text-center text-3xl font-extrabold">
            Sign in to your account
          </h2>
        </div>
        <div v-if="errorMessage" class="text-red-500 text-center">
          {{ errorMessage }}
        </div>
        <div class="mt-8 space-y-6" action="#" method="POST">
          <input type="hidden" name="remember" value="true" />
          <div class="rounded-md shadow-sm -space-y-px">
            <div>
              <label for="email-address" class="sr-only">Email address</label>
              <input
                id="email-address"
                v-model="email"
                name="email"
                type="email"
                autocomplete="email"
                required
                class="appearance-none rounded-none relative block w-full px-3 py-2 border border-gray-300 placeholder-gray-500 text-gray-900 sm:text-sm hover:border-indigo-500 hover:shadow-md"
                placeholder="Email address"
              />
            </div>
            <div>
              <label for="password" class="sr-only">Password</label>
              <input
                id="password"
                v-model="password"
                name="password"
                type="password"
                autocomplete="new-password"
                required
                class="appearance-none rounded-none relative block w-full px-3 py-2 border border-gray-300 placeholder-gray-500 text-gray-900 sm:text-sm hover:border-indigo-500 hover:shadow-md"
                placeholder="Password"
              />
            </div>
          </div>

          <div>
            <button
              type="submit"
              class="group relative w-full flex justify-center py-2 px-4 border border-transparent text-sm font-medium rounded-md text-white bg-black hover:bg-gray-800 focus:outline-none hover:shadow-md"
              @click="loginUser()"
            >
              Sign in
            </button>
          </div>
        </div>

        <div class="text-sm">
          <p class="mt-2">
            Don't have an account ?
            <a
              href="/register"
              class="font-medium text-indigo-600 hover:text-indigo-500"
            >
              Register here
            </a>
          </p>
        </div>
      </div>
    </section>
  </div>
</template>

<script setup>
const router = useRouter();
const email = ref("");
const password = ref("");
const supabase = useSupabaseClient();
const errorMessage = ref(null);

async function loginUser() {
  try {
    const { data, error } = await supabase.auth.signInWithPassword({
      email: email.value,
      password: password.value,
    });
    if (error) {
      throw error;
    } else {
      router.push("/");
    }
  } catch (error) {
    errorMessage.value = error.message;
  }
}
</script>
