<template>
  <div>
    <Navbar />
    <section class="flex items-center justify-center py-100 sm:px-6 lg:px-8">
      <div class="max-w-md w-full space-y-8">
        <div>
          <h2 class="mt-6 text-center text-3xl font-extrabold">
            Update Password
          </h2>
        </div>
        <div v-if="errorMessage" class="text-red-500 text-center">
          {{ errorMessage }}
        </div>
        <div class="mt-8 space-y-6" action="#" method="POST">
          <input type="hidden" name="remember" value="true" />
          <div class="rounded-md shadow-sm -space-y-px">
            <div>
              <label for="password" class="sr-only">New Password</label>
              <input
                id="password"
                v-model="NewPassword"
                name="password"
                type="password"
                autocomplete="password"
                required
                class="appearance-none rounded-none relative block w-full px-3 py-2 border border-gray-300 placeholder-gray-500 text-gray-900 sm:text-sm hover:border-indigo-500 hover:shadow-md"
                placeholder="New Password"
              />
            </div>
            <div>
              <label for="confirm-password" class="sr-only"
                >Confirm Password</label
              >
              <input
                id="confirm-password"
                v-model="NewConfirmPassword"
                name="confirm-password"
                type="password"
                autocomplete="confirm-password"
                required
                class="appearance-none rounded-none relative block w-full px-3 py-2 border border-gray-300 placeholder-gray-500 text-gray-900 sm:text-sm hover:border-indigo-500 hover:shadow-md"
                placeholder="Confirm Password"
              />
            </div>
          </div>

          <div>
            <button
              type="submit"
              class="group relative w-full flex justify-center py-2 px-4 border border-transparent text-sm font-medium rounded-md text-white bg-black hover:bg-gray-800 focus:outline-none hover:shadow-md"
              @click="resetPassword()"
            >
              Reset Password
            </button>
          </div>
        </div>

        <div class="text-sm">
          <p class="mt-2">
            Remembered your password ?
            <a
              href="/login"
              class="font-medium text-indigo-600 hover:text-indigo-500"
            >
              Sign in here
            </a>
          </p>
        </div>
      </div>
    </section>
  </div>
</template>

<script setup>
const router = useRouter();
const supabase = useSupabaseClient();
const errorMessage = ref(null);
const NewPassword = ref(null);
const NewConfirmPassword = ref(null);

async function resetPassword() {
  if (NewPassword.value !== NewConfirmPassword.value) {
    errorMessage.value = "Passwords do not match";
    return;
  }
  try {
    const { data, error } = await supabase.auth.updateUser({
      password: NewPassword.value,
    });
    if (error) {
      throw error;
    } else {
      alert("Password updated successfully");
      console.log("Password updated successfully");
      router.push("/");
    }
  } catch (error) {
    console.log("Error updating password:", error.message);
    errorMessage.value = error.message;
  }
}
</script>
