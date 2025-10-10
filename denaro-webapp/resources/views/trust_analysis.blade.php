@extends('layouts.app')

@section('title', 'Web Trust Analysis Tool')

@section('content')
    <h1 class="h3">Web Trust Analysis Tool</h1>
    <p class="text-muted">Coming soon.</p>

    <form method="POST" action="{{ route('trust.analyze') }}">
    {{-- <form method="POST" action=""> --}}
        @csrf
        <label for="url">Enter website link:</label>
        <input type="text" name="url" id="url" required>
        <button type="submit">Analyze</button>
    </form>
    
    @if(isset($analysisResult))
        <h2>Analysis Result</h2>
        <pre>{{ print_r($analysisResult, true) }}</pre>
    @endif
    
@endsection


