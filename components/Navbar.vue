<template>
    <div>
        <nav class="navbar flex justify-between items-center p-4 bg-white shadow-md grid grid-cols-3 gap-4">
            <div class="nav_left flex justify-start items-center space-x-4">
                <p class="nav_item font-bold"><a href="/">Home</a></p>
                <p class="nav_item font-bold"><a href="/collection">Collection</a></p>
                <p class="nav_item font-bold"><a href="/wishlist">Wishlist</a></p>
            </div>
            <div class="div_header flex justify-center items-center">
                <img class="logo w-20" href="/" src="../img/logo.png" alt="logo" />
            </div>
            <div class="nav_right flex justify-end items-center">
                <p class="login font-bold"><a href="/login">LOGIN</a></p>
            </div>
        </nav>
    </div>
</template>
