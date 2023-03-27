<script setup>

     import { ref, reactive, computed, onMounted } from 'vue'

    import { storeToRefs } from 'pinia'
    import { useAuthorStore } from '../store/authors'

    const { authors, loading, error } = storeToRefs(useAuthorStore())

    const { fetchAuthors } = useAuthorStore()

    onMounted(() => {
        fetchAuthors()
    })

    const state = ref(true)

    const alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']

    function filterByLetter(authors, letter) {
        const filterAuthors = authors.filter((item) => {
            return item.name.charAt(0).toLowerCase() === letter
        })
        return filterAuthors
    }

    function triAlpha(arr) {

        if (state.value) {
            arr.sort((a, b) => {
                    
                if (a < b) {
                    return -1
                }

                if (a > b) {
                    return 1
                }
                return 0

            })
        } else {
            arr.reverse((a, b) => {
                    
                if (a < b) {
                    return -1
                }

                if (a > b) {
                    return 1
                }
                return 0

            })
        }
        return arr
    }

</script>

<template>
    <main>
        <div v-if="loading">loading</div>

        <div v-if="error">{{ error.message }}</div>

        <div class="filters">
            <button @click="state = true">ascending</button>
            <button @click="state = false">descending</button>
        </div>

        <div class="author--container">
            <div 
                v-for="(letter, index) in triAlpha(alphabet)"
                :key="index"
            >

                <div 
                    v-if="filterByLetter(authors, letter).length"
                    class="lettrine">
                    {{ letter }}.
                </div>

                <div 
                    v-if="filterByLetter(authors, letter)" 
                    class="author--list"
                >
                
                    <div
                        v-for="author in filterByLetter(authors, letter)"
                        :key="author.id"
                        class="author--item"
                    >

                        <h2><RouterLink :to="`/author/${author.slug}`">{{ author.firstname ? author.firstname : null }} {{ author.name }}</RouterLink></h2>
                        <p>{{ author.bio }}</p>

                    </div>
                </div>

            </div>
        </div>
    </main>
</template>

<style scoped>

    .author--container {
        flex-direction: column;
    }

    .author--item {
        width: calc(100%/3);
    }

</style>