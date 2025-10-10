<nav class="navbar navbar-expand-lg navbar-dark bg-dark">
    <div class="container">
        <a class="navbar-brand" href="{{ url('/') }}">{{ config('app.name', 'Laravel') }}</a>
        <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#appNavbar" aria-controls="appNavbar" aria-expanded="false" aria-label="Toggle navigation">
            <span class="navbar-toggler-icon"></span>
        </button>

        <div class="collapse navbar-collapse" id="appNavbar">
            <ul class="navbar-nav ms-auto mb-2 mb-lg-0">
                {{-- TODO: Create more understandable links --}}
                <li class="nav-item">
                    <a class="nav-link {{ request()->is('report-scam') ? 'active' : '' }}" href="{{ route('scam.report') }}">Report a scam</a>
                </li>
                <li class="nav-item">
                    <a class="nav-link {{ request()->is('scam-info') ? 'active' : '' }}" href="{{ route('scam.info') }}">Scam Info</a>
                </li>
                <li class="nav-item">
                    <a class="nav-link {{ request()->is('trust-analysis') ? 'active' : '' }}" href="{{ url('/trust-analysis') }}">Web Trust Analysis Tool</a>
                </li>
                @guest
                <li class="nav-item">
                    <a class="nav-link {{ request()->is('authenticate') ? 'active' : '' }}" href="{{ route('authenticate') }}">Login / Register</a>
                </li>
                @endguest
                @auth
                <li class="nav-item dropdown">
                    <a class="nav-link dropdown-toggle" href="#" id="userDropdown" role="button" data-bs-toggle="dropdown" aria-expanded="false">
                        {{ auth()->user()->name }}
                    </a>
                    <ul class="dropdown-menu dropdown-menu-end" aria-labelledby="userDropdown">
                        <li>
                            <form method="POST" action="{{ route('logout') }}" class="px-3 py-1">
                                @csrf
                                <button class="btn btn-link p-0">Logout</button>
                            </form>
                        </li>
                    </ul>
                </li>
                @endauth
            </ul>
        </div>
    </div>
    
</nav>
