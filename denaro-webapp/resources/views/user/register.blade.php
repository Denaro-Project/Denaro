@extends('layouts.app')

@section('title', 'Register')

@section('content')
    <div class="container">
        <div class="row justify-content-center" style="min-height:60vh;">
            <div class="col-md-6">
                <div class="card shadow-sm">
                    <div class="card-body">
                        <h3 class="mb-3">Create an account</h3>

                        <form method="POST" action="{{ route('register.post') }}">
                            @csrf

                            <div class="mb-3">
                                <label for="name" class="form-label">Name</label>
                                <input type="text" id="name" name="name" class="form-control @error('name') is-invalid @enderror" value="{{ old('name') }}" required autofocus>
                                @error('name')<div class="invalid-feedback">{{ $message }}</div>@enderror
                            </div>

                            <div class="mb-3">
                                <label for="email" class="form-label">Email</label>
                                <input type="email" id="email" name="email" class="form-control @error('email') is-invalid @enderror" value="{{ old('email') }}" required>
                                @error('email')<div class="invalid-feedback">{{ $message }}</div>@enderror
                            </div>

                            <div class="mb-3">
                                <label for="password" class="form-label">Password</label>
                                <input type="password" id="password" name="password" class="form-control @error('password') is-invalid @enderror" required>
                                @error('password')<div class="invalid-feedback">{{ $message }}</div>@enderror
                            </div>

                            <div class="mb-3">
                                <label for="password_confirmation" class="form-label">Confirm Password</label>
                                <input type="password" id="password_confirmation" name="password_confirmation" class="form-control" required>
                            </div>

                            <div class="d-flex justify-content-between align-items-center">
                                <a href="{{ route('authenticate') }}" class="small">Back</a>
                                <button type="submit" class="btn btn-success">Create account</button>
                            </div>
                        </form>
                    </div>
                </div>
            </div>
        </div>
    </div>

@endsection
