@extends('layouts.app')

@section('title', 'Authenticate')

@section('content')
    <div class="container">
        <div class="row justify-content-center align-items-center" style="min-height:60vh;">
            <div class="col-md-6">
                <div class="card shadow-sm">
                    <div class="card-body text-center">
                        <h2 class="mb-1">Welcome to {{ config('app.name', 'Denaro') }}</h2>
                        <p class="text-muted">Please sign in or create an account to access the full features. You can also continue as a guest.</p>

                        <div class="d-grid gap-2 my-4">
                            <a href="{{ route('login') }}" class="btn btn-primary btn-lg">Login</a>
                            <a href="{{ route('register') }}" class="btn btn-outline-secondary btn-lg">Register</a>
                            <a href="{{ url('/home') }}" class="btn btn-link btn-lg">Continue as Guest</a>
                        </div>

                        <p class="small text-muted mt-3">By continuing you agree to our terms. Guests may have limited access.</p>
                    </div>
                </div>
            </div>
        </div>
    </div>

@endsection
