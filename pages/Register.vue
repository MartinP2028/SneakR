<template>
  <div>
    <Navbar />
    <section
      class="min-h-screen flex items-center justify-center py-12 px-4 sm:px-6 lg:px-8"
    >
      <div class="max-w-md w-full space-y-8">
        <div>
          <h2 class="mt-6 text-center text-3xl font-extrabold">
            Register an account
          </h2>
        </div>
        <form class="mt-8 space-y-6" action="#" method="POST">
          <input type="hidden" name="remember" value="true" />
          <div class="rounded-md shadow-sm -space-y-px">
            <div>
              <label for="first-name" class="sr-only">First Name</label>
              <input
                id="first-name"
                name="first-name"
                type="text"
                autocomplete="given-name"
                required
                class="appearance-none rounded-none relative block w-full px-3 py-2 border border-gray-300 placeholder-gray-500 text-gray-900 rounded-t-md focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 focus:z-10 sm:text-sm hover:border-indigo-500 hover:ring-indigo-500 hover:shadow-md"
                placeholder="First Name"
              />
            </div>
            <div>
              <label for="last-name" class="sr-only">Last Name</label>
              <input
                id="last-name"
                name="last-name"
                type="text"
                autocomplete="family-name"
                required
                class="appearance-none rounded-none relative block w-full px-3 py-2 border border-gray-300 placeholder-gray-500 text-gray-900 focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 focus:z-10 sm:text-sm hover:border-indigo-500 hover:ring-indigo-500 hover:shadow-md"
                placeholder="Last Name"
              />
            </div>
            <div>
              <label for="email-address" class="sr-only">Email address</label>
              <input
                id="email-address"
                name="email"
                type="email"
                autocomplete="email"
                required
                class="appearance-none rounded-none relative block w-full px-3 py-2 border border-gray-300 placeholder-gray-500 text-gray-900 focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 focus:z-10 sm:text-sm hover:border-indigo-500 hover:ring-indigo-500 hover:shadow-md"
                placeholder="Email address"
              />
            </div>
            <div>
              <label for="password" class="sr-only">Password</label>
              <input
                id="password"
                name="password"
                type="password"
                autocomplete="new-password"
                required
                class="appearance-none rounded-none relative block w-full px-3 py-2 border border-gray-300 placeholder-gray-500 text-gray-900 focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 focus:z-10 sm:text-sm hover:border-indigo-500 hover:ring-indigo-500 hover:shadow-md"
                placeholder="Password"
              />
            </div>
            <div>
              <label for="confirm-password" class="sr-only"
                >Confirm Password</label
              >
              <input
                id="confirm-password"
                name="confirm-password"
                type="password"
                autocomplete="new-password"
                required
                class="appearance-none rounded-none relative block w-full px-3 py-2 border border-gray-300 placeholder-gray-500 text-gray-900 rounded-b-md focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 focus:z-10 sm:text-sm hover:border-indigo-500 hover:ring-indigo-500 hover:shadow-md"
                placeholder="Confirm Password"
              />
            </div>
          </div>

          <div>
            <button
              type="submit"
              class="group relative w-full flex justify-center py-2 px-4 border border-transparent text-sm font-medium rounded-md text-white bg-indigo-500 hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500 hover:shadow-md"
            >
              Register
            </button>
          </div>
        </form>

        <div class="text-sm">
          <p class="mt-2">
            Already have an account?
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
