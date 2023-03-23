<script setup>

    import { storeToRefs } from 'pinia'
    import { useAuthorStore } from '../store/authors'

    const { authors, loading, error } = storeToRefs(useAuthorStore())

    const { fetchAuthors } = useAuthorStore()

    fetchAuthors()

    const alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']

    function filterByLetter(authors, letter) {
        const filterAuthors = authors.filter((item) => {
            return item.name.charAt(0).toLowerCase() === letter
        })
        return filterAuthors
    }

</script>

<template>
    <main>
        <div v-if="loading">loading</div>

        <div v-if="error">{{  error.message }}</div>

        <div 
            v-for="(letter, index) in alphabet"
            :key="index"
        >

            <div 
                v-if="filterByLetter(authors, letter).length"
                class="lettrine">
                {{ letter }}.
            </div>

            <div 
                v-if="filterByLetter(authors, letter)" 
                class="author"
            >
            
                <div
                    v-for="author in filterByLetter(authors, letter)"
                    :key="author.id"
                    class="author--item"
                >

                    <h2><RouterLink :to="`/author/${author.slug}`">{{ author.firstname ? author.firstname : null }} {{ author.name }}</RouterLink></h2>
                    <p class="description">{{ author.bio }}</p>

                </div>
            </div>

        </div>
    </main>
</template>