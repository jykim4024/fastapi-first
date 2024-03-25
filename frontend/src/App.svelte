<script>
    import Router from 'svelte-spa-router'
    import Home from "./routes/Home.svelte"
    import Detail from "./routes/Detail.svelte"
    import QuestionCreate from "./routes/QuestionCreate.svelte"
    import Navigation from "./components/Navigation.svelte"
    import UserCreate from "./routes/UserCreate.svelte"
    import UserLogin from "./routes/UserLogin.svelte"

    const routes = {
        '/': Home,
        '/detail/:question_id': Detail,
        '/question-create' : QuestionCreate,
        '/user-create' : UserCreate,
        '/user-login' : UserLogin,
    }
</script>

<Navigation />
<Router {routes} />



<!-- 1.분기문
{#if 조건문1}
    <p>조건문1에 해당하면 실행</p>
{:else if 조건문2}
    <p>조건문2에 해당하면 실행</p>
{:else}
    <p>조건문1,2 모두 해당하지 않으면 실행</p>
{/if}

2.반복문
{#each list as item, index}
    <p>순서 : {index}</p>
    <p>{item}</p>
{/each} -->