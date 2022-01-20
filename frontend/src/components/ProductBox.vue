<template>
    
    <div class="column is-3">

        <div class="box">
            <figure class="image mb-4">
                <img v-bind:src="product.get_thumbnail">
            </figure>

            <h3 class="is-size-4"><strong>{{ product.name }}</strong></h3>
            <p class="is-size-6 has-text-grey">${{ product.price }}</p>

            
            <div class="field is-grouped">
                <p class="control">
                    <router-link v-bind:to="product.get_absolute_url" class="button is-small is-dark mt-4">Home</router-link>
                </p>
                <p class="control">
                    <button class="button is-link  is-small mt-4">
                        <span class="icon">
                            <i class="fab fa-discord"></i>
                        </span>
                        <span>discord</span>
                    </button>
                </p>
                <p class="control">
                    <button class="button is-primary is-small mt-4">
                        <span class="icon">
                            <i class="fab fa-twitter"></i>
                        </span>
                        <span>twitter</span>
                    </button>
                </p>
            </div>
            
        </div>
    </div>
</template>

<script>
export default {
    name: 'ProductBox',
    props: {
        product: Object
    }
}
</script>

<style scoped>
  .image {
    margin-top: -1.25rem;
    margin-left: -1.25rem;
    margin-right: -1.25rem;
  }
</style>