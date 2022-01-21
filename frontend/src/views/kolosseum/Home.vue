<template>
  <div class="home">
    <section class="hero is-medium has-text-white mb-6">
        <div class="hero-body has-text-centered">
            <p class="title mb-6 is-size-1">
                Klaytn NFT World
            </p>
            <p class="subtitle">
                Kolosseum !
            </p>
        </div>
    </section>

    <div class="columns is-multiline">

      <ProductBox 
        v-for="product in latestProducts"
        v-bind:key="product.id"
        v-bind:product="product" />
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import ProductBox from '@/components/kolosseum/ProductBox'

export default {
  name: 'Home',
  data() {
    return {
      latestProducts: []
    }
  },
  components: {
    ProductBox
  },
  
  mounted() {
    this.getLatestProducts()

    document.title = 'Kolosseum'
  },
  methods: {
    async getLatestProducts() {
      this.$store.commit('setIsLoading', true)

      axios
        .get('/api/v1/latest-products/')
        .then(response => {
          this.latestProducts = response.data

          console.log(this.latestProducts.length)
        })
        .catch(error => {
          console.log(error)
        })

        this.$store.commit('setIsLoading', false)
    }
  }
}
</script>

