<!doctype html>
<html lang="en">
    <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <meta name="csrf-token" content="{{ csrf_token() }}">

        <title>@yield('title', config('app.name', 'Laravel'))</title>

        <!-- Bootstrap CSS -->
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">

        <!-- App styles (optional) -->
        {{-- @vite(['resources/css/app.css']) --}}
    </head>
    <body class="bg-light">
        @include('partials.navigation_bar')

        <main class="container py-4">
            @include('partials.alert')
            @yield('content')
        </main>

        <footer class="text-center text-muted py-3">
            <small>&copy; {{ date('Y') }} {{ config('app.name') }}</small>
        </footer>

        <!-- Bootstrap JS (with Popper) -->
        <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js"></script>

        <!-- App scripts (optional) -->
        {{-- @vite(['resources/js/app.js']) --}}
    </body>
</html>
