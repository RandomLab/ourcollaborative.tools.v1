<script setup>

    import { reactive, ref } from 'vue'

    import { storeToRefs } from 'pinia'
    import { useSearchStore } from '../store/search'

    import Results from '../components/Results.vue'

    const { notions, projects, authors, references, loading, error } = storeToRefs(useSearchStore())

    const { fetchSearch } = useSearchStore()

    const search = reactive({
        word: '',
    })

    function launchSearch() {
        fetchSearch(search.word)
        search.word = ''
    }

</script>

<template>
    <main>
        
        <div class="search-index">
            <h2>Search through all</h2>
            <input 
                type="text"
                placeholder="keyword"
                v-model="search.word"
                @keyup.enter="launchSearch"
            >
        </div>

        <div class="search-index-mobile">
            <input 
                type="text"
                placeholder="Search through all"
                v-model="search.word"
            >
            <button @click="launchSearch">GO</button>
        </div>

        <div class="loading" v-if="loading">loading</div>
        <div class="error" v-if="error">{{ error.message }}</div>

        <!-- notions -->

        <div 
            v-if="notions.length > 0" 
            class="search-results"
        >

            <div
                v-for="notion in notions"
                :key="notion.id"
            >
                <results :result="notion"></results>

            </div>

        </div>

        <!-- project -->

        <div 
            v-if="projects.length > 0" 
            class="search-results"
        >

            <div
                v-for="project in projects"
                :key="project.id"
            >
                <results :result="project"></results>

            </div>

        </div>

        <!-- author -->

        <div 
            v-if="authors.length > 0" 
            class="search-results"
        >

            <div
                v-for="author in authors"
                :key="author.id"
            >
                <results :result="author"></results>

            </div>

        </div>


        <div v-else class="no-result">no results</div>

    </main>
   

</template>