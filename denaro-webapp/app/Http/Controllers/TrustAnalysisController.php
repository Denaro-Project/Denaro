<?php

namespace App\Http\Controllers;

use App\Http\Controllers\Controller;
use Illuminate\Support\Facades\Http;
use Illuminate\Http\Request;

class TrustAnalysisController extends Controller
{
    //
    public function analyze(Request $request)
    {
        $url = $request->input('url');

        // Send URL to Python API
        $response = Http::post('http://127.0.0.1:5000/analyze', [ //Replace with your Python API endpoint
            'url' => $url,
        ]);

        $analysisResult = $response->json();

        // Pass result back to the view
        return view('trust_analysis', compact('analysisResult'));
    }
}
