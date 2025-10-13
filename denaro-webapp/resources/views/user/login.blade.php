@extends('layouts.app')

@section('title', 'Login')

@section('content')
    <div class="container">
        <div class="row justify-content-center" style="min-height:60vh;">
            <div class="col-md-6">
                <div class="card shadow-sm">
                    <div class="card-body">
                        <h3 class="mb-3">Login</h3>

                        <form method="POST" action="{{ route('login.post') }}">
                            @csrf

                            <div class="mb-3">
                                <label for="email" class="form-label">Email</label>
                                <input type="email" id="email" name="email" class="form-control @error('email') is-invalid @enderror" value="{{ old('email') }}" required autofocus>
                                @error('email')<div class="invalid-feedback">{{ $message }}</div>@enderror
                            </div>

                            <div class="mb-3">
                                <label for="password" class="form-label">Password</label>
                                <input type="password" id="password" name="password" class="form-control @error('password') is-invalid @enderror" required>
                                @error('password')<div class="invalid-feedback">{{ $message }}</div>@enderror
                            </div>

                            <div class="d-flex justify-content-between align-items-center mb-3">
                                <div class="form-check">
                                    <input class="form-check-input" type="checkbox" id="remember" name="remember" value="1">
                                    <label class="form-check-label" for="remember">Remember me</label>
                                </div>
                                <a href="{{ route('authenticate') }}" class="small">Back</a>
                            </div>

                            <div class="d-grid">
                                <button type="submit" class="btn btn-primary">Login</button>
                            </div>
                        </form>
                    </div>
                </div>
            </div>
        </div>
    </div>

@endsection
