"use client";

import * as React from "react";
import { useState } from "react";

import { Button } from "@/components/ui/button";
import {
  Card,
  CardContent,
  CardDescription,
  CardHeader,
  CardTitle,
} from "@/components/ui/card";
import { Input } from "@/components/ui/input";
import { Label } from "@/components/ui/label";
import { Loader2 } from "lucide-react";

export function RequestSalaryCard() {
  const [isLoading, setIsLoading] = useState(false);
  const [result, setResult] = useState<string | null>(null);
  
  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    setIsLoading(true);
    setResult(null);
    
    // Simulare un'analisi del CV per 5 secondi
    setTimeout(() => {
      setIsLoading(false);
      setResult("Queste sono le tue informazioni:\nRuolo: frontend engineer\nEsperienza: 1-3 anni\nLocation: Milano");
    }, 5000);
  }

  return (
    <Card className="w-[400px] bg-white">
      <CardHeader>
        <CardTitle>Salary Benchmark Analysis</CardTitle>
        <CardDescription>Upload your CV to discover your market value.</CardDescription>
      </CardHeader>
      
      <CardContent>
        {!isLoading && !result && (
          <form onSubmit={handleSubmit}>
            <div className="flex flex-col space-y-4">
              <div className="flex flex-col space-y-1.5">
                <Label htmlFor="cv">Upload Your CV</Label>
                <Input id="cv" type="file" accept=".pdf,.doc,.docx" required />
                <p className="text-sm text-gray-500 mt-1">
                  We&apos;ll analyze your CV to provide accurate salary insights.
                  Your CV won&apos;t be stored permanently for privacy reasons.
                </p>
              </div>
              
              <Button 
                type="submit"
                className="w-full mt-4"
              >
                Submit
              </Button>
            </div>
          </form>
        )}
        
        {isLoading && (
          <div className="flex flex-col items-center justify-center py-8 space-y-4">
            <Loader2 className="h-8 w-8 animate-spin text-primary" />
            <p className="text-muted-foreground">Analyzing your CV...</p>
          </div>
        )}
        
        {result && (
          <div className="flex flex-col space-y-4 py-4">
            <div className="rounded-lg bg-muted p-4">
              <h3 className="font-medium mb-2">Analysis Results</h3>
              <pre className="whitespace-pre-wrap text-sm">
                {result}
              </pre>
            </div>
            <Button 
              variant="outline" 
              onClick={() => {
                setResult(null);
              }}
              className="w-full"
            >
              Upload Another CV
            </Button>
          </div>
        )}
      </CardContent>
    </Card>
  );
}