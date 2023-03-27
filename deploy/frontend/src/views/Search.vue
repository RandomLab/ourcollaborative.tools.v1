<script setup>

    import { reactive } from 'vue'

    import { storeToRefs } from 'pinia'
    import { useSearchStore } from '../store/search'

    import Results from '../components/Results.vue'

    const { results, loading, error } = storeToRefs(useSearchStore())

    const { fetchSearch } = useSearchStore()

    const search = reactive({
        word: '',
        type: 'projects'
    })

    function lauchSearch() {
        fetchSearch(search.word, search.type)
        search.word = ''
    }

</script>

<template>
    <main>
        
        <div class="search-index">
            <h2>Search through all <button @click="search.type = 'projects'">projects</button> or <button @click="search.type = 'notions'">notions</button></h2>
            <input 
                type="text"
                :placeholder="`search in ${search.type}`"
                v-model="search.word"
                @keyup.enter="lauchSearch"
            >
        </div>

        <div v-if="loading">loading</div>
        <div v-if="error">{{  error.message }}</div>

        <div 
            v-if="results.length > 0" 
            class="search-results"
        >

            <div
                v-for="result in results"
                :key="result.id"
            >
                <results :result="result"></results>

            </div>

        </div>

        <div v-else class="no-result">no results</div>

    </main>
   

</template>