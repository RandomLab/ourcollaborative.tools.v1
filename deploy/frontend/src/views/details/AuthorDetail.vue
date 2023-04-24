<script setup>

    import { ref, reactive, computed, onMounted } from 'vue'

    import { useRouter } from 'vue-router'

    import { storeToRefs } from 'pinia'
    import { useAuthorStore } from '../../store/authors'

    import Cross from '../../components/utils/Cross.vue'

    import AuthorProjects from '../../components/author/AuthorProjects.vue'

    const { authors, author, loading, error } = storeToRefs(useAuthorStore())

    const { fetchAuthors, setAuthor } = useAuthorStore()

    onMounted(() => {
        fetchAuthors()
        setAuthor()
    })

    const router = useRouter()

    const alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']

    function filterByLetter(authors, letter) {
        const filterAuthor = authors.filter((item) => {
            return item.name.charAt(0).toLowerCase() === letter
        })
        return filterAuthor
    }

</script>

<template>

    <main>
        <div class="loading" v-if="loading">Loading author</div>
        
        <div class="error" v-if="error">{{ error.message }}</div>

        <div class="author--container">
            <div class="author--left">
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
                        class="author--list"
                    >
                        <div
                            v-for="author in filterByLetter(authors, letter)"
                            :key="author.id"
                            class="author--item"
                        >

                            <h2>
                                <router-link
                                    @click="setAuthor(author)"
                                    :to="`${author.slug}`"    
                                >
                                    {{ author.group ? null : author.firstname }} {{ author.name }}
                                </router-link>
                            </h2>
                                
                        </div>
                    
                    
                    </div>

                </div>
            </div>

            <div class="author--right">

                <cross
                    @click="router.push({ name: 'authors'})" 
                    width="50" 
                    height="50"
                ></cross>

                <author-projects></author-projects>
            </div>

       </div>

    </main>
    
</template>

<style scoped>

    .author--list {
        flex-direction: column;
    }

    .author--item {
        width: 100%;
    }

</style>