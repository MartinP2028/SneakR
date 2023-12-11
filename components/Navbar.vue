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
        <p class="login font-bold"><a href="/login">LOGIN</a></p>
      </div>
    </nav>
  </div>
</template>
