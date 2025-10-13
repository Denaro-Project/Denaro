<nav class="navbar navbar-expand-lg navbar-dark bg-dark">
    <div class="container">
        <a class="navbar-brand" href="{{ url('/') }}">{{ config('app.name', 'Denaro') }}</a>
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
                    <a class="nav-link d-flex align-items-center {{ request()->is('authenticate') ? 'active' : '' }}" href="{{ route('authenticate') }}" aria-label="Login or Register">
                        {{-- Default profile avatar (SVG) --}}
                        <span class="d-inline-block rounded-circle bg-secondary overflow-hidden" style="width:32px;height:32px;">
                            <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" class="text-light" width="32" height="32" role="img" aria-hidden="true">
                                <path d="M12 12c2.761 0 5-2.239 5-5s-2.239-5-5-5-5 2.239-5 5 2.239 5 5 5zm0 2c-3.866 0-7 3.134-7 7h2c0-2.761 2.239-5 5-5s5 2.239 5 5h2c0-3.866-3.134-7-7-7z"/>
                            </svg>
                        </span>
                    </a>
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
